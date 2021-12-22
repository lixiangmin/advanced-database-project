import csv
import json
import random
import re
import time

import pandas as pd
from pyquery import PyQuery as pq  # 爬虫库
import requests
from setuptools._vendor.pyparsing import unichr


def parse_data(data_filename, data_type, data_index, data_id="id", neglect=None):
    if neglect is None:
        neglect = [19730, 29503, 35587]
    with open("data/" + data_filename + ".csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        next(reader)
        file = open("parse_files/" + data_type + ".csv", "w")
        writer = csv.writer(file)
        header = ""
        ids = []
        for i, read_data in enumerate(reader):
            if len(read_data) <= data_index:
                continue
            datas = eval(read_data[data_index])
            if not isinstance(datas, list) or i in neglect:
                print(i, read_data)
                continue
            for data in datas:
                if header == "":
                    header = data.keys()
                    writer.writerow(header)
                if not ids.__contains__(data.get(data_id)):
                    writer.writerow(data.values())
                    ids.append(data.get(data_id))
                else:
                    print("repeated_data:")
                    print(data.values())
        print("-----------------------      end " + data_type + " parsing      -------------------------------")


def parse_meta_data():
    neglect = [19730, 29503, 35587]
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        file = open("parse_files/movies_metadata.csv", "w")
        writer = csv.writer(file)
        header = next(reader)
        writer.writerow(header)
        idList = []
        dataList = []
        for i, data in enumerate(reader):
            if i in neglect:
                continue
            if data[5] in idList:
                idx = idList.index(data[5])
                data = dataList[idx]
            idList.append(data[5])
            dataList.append(data)
            writer.writerow(data)
        print("-----------------------      end movies_meta_data parsing      -------------------------------")


def parse_necessary_data():
    parse_data("movies_metadata", "genres", 3)
    parse_data("movies_metadata", "production_companies", 12)
    parse_data("movies_metadata", "production_countries", 13, "iso_3166_1")
    parse_data("movies_metadata", "spoken_languages", 17, "iso_639_1")
    parse_data("credits", "crews", 1)
    parse_data("credits", "casts", 0)
    parse_data("keywords", "keywords", 1)
    parse_meta_data()


def generate_relations_by_movies_metadata(relation_name, data_type, data_index, data_id, relation, neglect=None):
    if neglect is None:
        neglect = [19730, 29503, 35587]
    file = open("relations/" + relation_name + ".csv", "w")
    writer = csv.writer(file)
    writer.writerow(["movieId", data_type + "Id", "relation"])
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as movies_metadata_file:
        reader = csv.reader(movies_metadata_file)
        next(reader)
        for i, movie_metadata in enumerate(reader):
            if len(movie_metadata) != 24 or i in neglect:
                continue
            movie_id = movie_metadata[5]
            if len(movie_metadata[data_index]) != 0:
                items = eval(movie_metadata[data_index])
                for item in items:
                    row = [movie_id, item.get(data_id), relation]
                    writer.writerow(row)
    print("-----------------------      finish " + relation_name + " generating      -------------------------------")


def generate_relations_by_movies_and_extra(relation_name, extra_file_path, extra_data_type, extra_data_index,
                                           extra_data_id,
                                           extra_data_movie_id_index, relation):
    file = open("relations/" + relation_name + ".csv", "w")
    writer = csv.writer(file)
    writer.writerow(["movieId", extra_data_type + "Id", "relation"])
    extra_file = open(extra_file_path, "r")
    extra_file_reader = csv.reader(extra_file)
    next(extra_file_reader)
    dict = {}
    for extra_data in extra_file_reader:
        dict[extra_data[extra_data_movie_id_index]] = eval(extra_data[extra_data_index])
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as movies_metadata_file:
        reader = csv.reader(movies_metadata_file)
        next(reader)
        for movie_metadata in reader:
            if len(movie_metadata) != 24:
                continue
            movie_id = movie_metadata[5]
            extra_data = dict.get(movie_id)
            if extra_data:
                for data in extra_data:
                    row = [movie_id, data.get(extra_data_id), relation]
                    writer.writerow(row)


def generate_relations():
    generate_relations_by_movies_metadata("genres_relation", "genre", 3, "id", "belong_to")
    generate_relations_by_movies_metadata("spoken_languages_relation", "language", 17, "iso_639_1", "speak")
    generate_relations_by_movies_metadata("production_countries_relation", "country", 13, "iso_3166_1", "product")
    generate_relations_by_movies_metadata("production_companies_relation", "company", 12, "id", "product")
    generate_relations_by_movies_and_extra("keywords_relation", "data/keywords.csv", "keyword", 1, "id", 0, "describe")
    generate_relations_by_movies_and_extra("crews_relation", "data/credits.csv", "crew", 1, "id", 2, "work_in")
    generate_relations_by_movies_and_extra("casts_relation", "data/credits.csv", "cast", 0, "id", 2, "act")


def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)


def merge(a_file, b_file, int_idx, efficient=False):
    big_file = open("data/" + a_file + ".csv", "r", encoding='UTF-8')
    big_file_reader = csv.reader(big_file)
    merged_file = open("parse_files/" + a_file + "_merged.csv", "w", encoding='UTF-8')
    merged_file_writer = csv.writer(merged_file)
    header = next(big_file_reader)
    merged_file_writer.writerow(header)
    big_file_data = []
    for row in big_file_reader:
        for idx in int_idx:
            if row[idx] != '':
                row[idx] = int(row[idx])
        big_file_data.append(row)
    with open("data/" + b_file + ".csv", "r", encoding='UTF-8') as small_file:
        small_file_reader = csv.reader(small_file)
        next(small_file_reader)
        row_num = row_count("data/" + b_file + ".csv")
        if efficient is False:
            for small_file_data in small_file_reader:
                for idx in int_idx:
                    if small_file_data[idx] != '':
                        small_file_data[idx] = int(small_file_data[idx])
                if small_file_data not in big_file_data:
                    big_file_data.append(small_file_data)
            big_file_data.sort()
            merged_file_writer.writerows(big_file_data)
        else:
            is_small_end = False
            row = next(small_file_reader)
            for idx in int_idx:
                if row[idx] != '':
                    row[idx] = int(row[idx])
            i = 0
            while i < len(big_file_data):
                d = big_file_data[i]
                if is_small_end:
                    merged_file_writer.writerow(d)
                    i += 1
                else:
                    if d[0] < row[0] or (d[0] == row[0] and d[1] < row[1]):
                        merged_file_writer.writerow(d)
                        i += 1
                        continue
                    elif d[0] > row[0] or (d[0] == row[0] and d[1] > row[1]):
                        merged_file_writer.writerow(row)
                        i -= 1
                    # 处理同一个人对同一部电影的多次评价，取最新的评价
                    else:
                        if int(d[3]) > int(row[3]):
                            merged_file_writer.writerow(d)
                        else:
                            merged_file_writer.writerow(row)
                    i += 1
                    # 处理small文件里最后一个没有写入的问题
                    if small_file_reader.line_num == row_num:
                        is_small_end = True
                        continue
                    row = next(small_file_reader)
                    for idx in int_idx:
                        if row[idx] != '':
                            row[idx] = int(row[idx])
    print("-----------------------      finish " + a_file + " generating      -------------------------------")


def merge_files():
    merge("links", "links_small", [0, 1, 2])
    merge("ratings", "ratings_small", [0, 1], efficient=True)


def generate_user():
    user_file = open("parse_files/user.csv", "w", encoding='UTF-8')
    user_file_writer = csv.writer(user_file)
    user_file_writer.writerow(["id", "name"])
    with open("parse_files/ratings_merged.csv", "r", encoding='UTF-8') as ratings:
        ratings_reader = csv.reader(ratings)
        header = next(ratings_reader)
        now_user_id = -1
        for rating in ratings_reader:
            user_id = rating[0]
            if user_id != now_user_id:
                name = get_name()
                user_file_writer.writerow([user_id, name])
                now_user_id = user_id


def get_name():
    '''随机生成名字'''
    xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危',
            '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍',
            '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁',
            '单', '杭', '洪',
            '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄',
            '麴', '家', '封',
            '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车',
            '侯', '宓', '蓬',
            '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景',
            '詹', '束', '龙',
            '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓',
            '蔺', '屠', '蒙',
            '池', '乔', '阴', '欎', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉',
            '宰', '郦', '雍',
            '舄', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴',
            '瞿', '阎', '充',
            '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都',
            '耿', '满', '弘',
            '匡', '国', '文', '寇', '广', '禄', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁',
            '勾', '敖', '融',
            '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查',
            '後', '荆', '红',
            '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟',
            '公羊',
            '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '钟离', '宇文', '长孙', '慕容', '鲜于', '闾丘',
            '司徒', '司空', '亓官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓跋', '夹谷', '宰父',
            '谷梁', '晋', '楚', '闫', '法', '汝', '鄢', '涂', '钦', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '岳', '帅',
            '缑',
            '亢', '况', '后', '有', '琴', '梁丘', '左丘', '东门', '西门', '商', '牟', '佘', '佴', '伯', '赏', '南宫', '墨', '哈', '谯', '笪',
            '年', '爱',
            '阳', '佟', '第五', '言', '福', '百', '家', '姓', '终', '延拓归宁', '爱新觉罗', '叶赫那拉', '呼延觉罗', '夏兰荇德', '古拉依尔', '韩克拉玛',
            '阿尔塔斯', '阿哈觉罗', '阿拉边前', '阿拉克塔', '阿拉克球', '阿勒巴齐', '阿鲁络特', '阿图拉墨', '阿颜觉罗', '敖拉托欣', '敖勒多尔', '巴雅尔齐',
            '拜英格哩', '宝里吉特', '贝亚吉尔', '毕拉达克', '博尔和罗', '博尔苏特', '博尔济克', '博尔济斯', '博古罗特', '博古罗克', '博勒卓克', '布吉尔根',
            '布雅穆齐', '察喇觉罗', '苍马尔纪', '达尔充阿', '达喇明安', '德特齐特', '都克塔理', '都瓦尔佳', '多尔塔喇', '额尔格济', '额尔格图', '额尔库勒',
            '额尔图特', '额穆特立', '鄂恩济特', '鄂尔绰络', '鄂尔克特', '鄂里木苏', '鄂苏尔瑚', '富尔库鲁', '噶必齐克', '噶尔噶斯', '格伦觉罗', '葛瓦依尔',
            '葛依克勒', '公吉喇特', '功格喇布', '古拉依尔', '郭尔罗斯', '郭尔罗特', '哈尔吉努', '哈尔图特', '哈勒塔喇', '哈思呼哩', '罕吉拉锦', '和脱果特',
            '赫锡赫理', '洪鄂罗特', '呼伦觉罗', '胡西哈尔', '瑚克锡勒', '瑚尔哈喇', '瑚尔哈苏', '瑚尔库尔', '瑚尔拉斯', '瑚克锡勒', '瑚拉巴斯', '瑚锡哈理',
            '华西哈里', '吉尔必斯', '嘉布塔喇', '喀尔拉哈', '喀尔诺特', '喀克锡理', '喀勒达苏', '喀什喀腾', '卡格依尔', '克穆楚特', '克穆齐特', '克伊克勒',
            '奎车里克', '阔齐图里', '玛哈依尔', '玛拉库尔', '玛拉依尔', '莽格努特', '蒙古尔济', '孟克宜勒', '谟勒齐哩', '墨尔达札', '墨尔乞特', '墨尔哲勒',
            '墨勒哲勒', '默讷赫尔', '木克得立', '那木都鲁', '尼阳尼雅', '钮祜禄布', '努尔哈拉', '齐尔博苏', '齐木克图', '齐普齐特', '齐普楚特', '奇尔果特',
            '撒玛吉尔', '萨尔图克', '萨勒珠特', '萨哈尔察', '萨哈勒济', '萨拉塔克', '萨拉特卓', '萨玛尔吉', '萨穆希尔', '色穆奇理', '舒克都哩', '舒善觉罗',
            '舒舒觉罗', '孙尼耀特', '索济雅喇', '索龙古斯', '索罗噶尔', '泰锡纳喇', '特尔吉尔', '通颜觉罗', '佟尼耀特', '图尔塔喇', '图罗鲁特', '托和尔秦',
            '旺古尔沁', '魏拉依尔', '翁吉勒金', '乌尔古宸', '乌尔杭阿', '乌尔瑚济', '乌济奇特', '乌里雅特', '乌朗哈特', '乌讷穆尔', '乌恰尔坎', '乌齐喜特',
            '吴济忒克', '吴札勒瑚', '武尔格齐', '武库登吉', '西林觉罗', '锡尔德特', '锡克济拉', '锡克特哩', '锡勒尔吉', '锡讷楚克', '席奇吉尔', '喜特勒那',
            '伊布齐特', '伊尔库勒', '伊克得里', '伊克明安', '玉尔库勒', '扎哈齐特', '扎哈苏沁', '札思瑚哩', '札雅札喇', '兆达尔汉', '郑讷鲁特', '卓巴鲁特',
            '卓尔古特', '卓尔和沁', '阿答尔斤', '阿勒呼目', '奥尔根千', '巴利厄兹', '巴落瓦支', '巴音托布', '巴亚基尔', '孛儿只斤', '布古鲁克', '彻尔济达',
            '绰尔齐岱', '答答尔歹', '达格赫兰', '达兰奈曼', '达瓦买提', '地阿勺普', '地哈勺普', '多托尔台', '恩柬司波', '噶玛拉木', '格沙斯日']
    ming1 = random.randint(19968, 40869)
    ming1 = unichr(ming1)
    ming2 = random.randint(19968, 40869)
    ming2 = unichr(ming2)
    name = random.choice(xing) + ming1 + ming2
    return name


def scrape_api(url):
    """爬取网页接口"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
    except requests.RequestException:
        return None


def parse_data_neo4j_import(data_filename, output_filename, int_idxs, float_idxs, ignore_idxs, primary_key_name,
                            primary_key="id", parse_primary_key=False):
    with open("parse_files/" + data_filename + ".csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        file = open("parse_neo4j_import_files/" + output_filename + ".csv", "w")
        writer = csv.writer(file)
        primary_key_idx = 0
        primary_keys = []
        header = []
        d = []
        for i, read_data in enumerate(reader):
            if i == 0:
                for j, head in enumerate(read_data):
                    if j in ignore_idxs:
                        continue
                    if head == primary_key:
                        primary_key_idx = j
                        header.append(primary_key + ":ID(" + primary_key_name + ")")
                    else:
                        if j in int_idxs:
                            header.append(head + ":int")
                        elif j in float_idxs:
                            header.append(head + ":float")
                        else:
                            header.append(head)
                print(header)
                writer.writerow(header)
            else:
                if parse_primary_key is True:
                    if read_data[primary_key_idx] in primary_keys:
                        continue
                    else:
                        primary_keys.append(read_data[primary_key_idx])
                sub_d = []
                for j, data in enumerate(read_data):
                    if j in ignore_idxs:
                        continue
                    sub_d.append(data)
                d.append(sub_d)
                # print(i)
        # d = [[i] for i in sorted(list(set(d)))]
        # print(len(d))
        writer.writerows(d)

    print("-----------------------  finish " + data_filename + "data parsing for neo4j import  -----------------------")


def parse_necessary_data_neo4j_import():
    parse_data_neo4j_import("movies_metadata", "movies_metadata_neo4j_import", [2, 15, 16, 23], [10, 22],
                            [1, 3, 12, 13, 17], "MOVIE-ID", "id")
    parse_data_neo4j_import("casts", "casts_neo4j_import", [0, 3, 6], [], [], "CAST-ID", "id")
    parse_data_neo4j_import("production_companies", "production_companies_neo4j_import", [], [], [], "COMPANY-ID", "id")
    parse_data_neo4j_import("production_countries", "production_countries_neo4j_import", [], [], [], "COUNTRY-ID",
                            "iso_3166_1")
    parse_data_neo4j_import("crews", "crews_neo4j_import", [2], [], [], "CREW-ID", "id")
    parse_data_neo4j_import("genres", "genres_neo4j_import", [], [], [], "GENRE-ID", "id")
    parse_data_neo4j_import("keywords", "keywords_neo4j_import", [], [], [], "KEYWORD-ID", "id")
    parse_data_neo4j_import("spoken_languages", "spoken_languages_neo4j_import", [], [], [], "LANGUAGE-ID", "iso_639_1")
    parse_data_neo4j_import("ratings_merged", "user_neo4j_import", [], [], [1, 2, 3], "USER-ID", "userId",
                            parse_primary_key=True)


def generate_relations_neo4j_import(data_filename, output_filename, start_id, end_id, start_name, end_name, int_idxs,
                                    float_idxs, ignore_idxs, dir="relations/"):
    with open(dir + data_filename + ".csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        file = open("relations_neo4j_import_files/" + output_filename + ".csv", "w")
        writer = csv.writer(file)
        header = []
        for i, read_data in enumerate(reader):
            if i == 0:
                for j, head in enumerate(read_data):
                    if j in ignore_idxs:
                        continue
                    if head == start_id:
                        header.append(":START_ID(" + start_name + ")")
                    elif head == end_id:
                        header.append(":END_ID(" + end_name + ")")
                    else:
                        if j in int_idxs:
                            header.append(head + ":int")
                        elif j in float_idxs:
                            header.append(head + ":float")
                        else:
                            header.append(head)
                print(header)
                writer.writerow(header)
            else:
                d = []
                for j, data in enumerate(read_data):
                    if j in ignore_idxs:
                        continue
                    d.append(data)
                writer.writerow(d)
                # print(i)

    print(
        "-----------------------  finish " + data_filename + "relation parsing for neo4j import  -----------------------")


def generate_relations_neo4j_import_batch():
    generate_relations_neo4j_import("casts_relation", "casts_relation_neo4j_import", "castId", "movieId", "CAST-ID",
                                    "MOVIE-ID", [], [], [])
    generate_relations_neo4j_import("crews_relation", "crews_relation_neo4j_import", "crewId", "movieId", "CREW-ID",
                                    "MOVIE-ID", [], [], [])
    generate_relations_neo4j_import("genres_relation", "genres_relation_neo4j_import", "movieId", "genreId", "MOVIE-ID",
                                    "GENRE-ID", [], [], [])
    generate_relations_neo4j_import("keywords_relation", "keywords_relation_neo4j_import", "keywordId", "movieId",
                                    "KEYWORD-ID", "MOVIE-ID", [], [], [])
    generate_relations_neo4j_import("production_companies_relation", "production_companies_relation_neo4j_import",
                                    "companyId", "movieId", "COMPANY-ID", "MOVIE-ID", [], [], [])
    generate_relations_neo4j_import("production_countries_relation", "production_countries_relation_neo4j_import",
                                    "countryId", "movieId", "COUNTRY-ID", "MOVIE-ID", [], [], [])
    generate_relations_neo4j_import("spoken_languages_relation", "spoken_languages_relation_neo4j_import", "movieId",
                                    "languageId", "MOVIE-ID", "LANGUAGE-ID", [], [], [])
    generate_relations_neo4j_import("ratings_merged", "ratings_merged_neo4j_import", "userId", "movieId", "USER-ID",
                                    "MOVIE-ID", [3], [2], [], dir="parse_files/")


print("-----------------------      start data parsing      -------------------------------")


def get_movie_png(movie_name):
    """获取每部电影的封面图片的url"""
    # imdb搜索
    search_url = f'https://www.imdb.com/find?q={movie_name}'
    response = scrape_api(search_url)
    if response is None:
        return None
    doc = pq(response.text)
    poster_url = doc('.findList tr td a img').attr('src')
    if poster_url is None:
        return None
    else:
        return poster_url
    # imdb封面url链接获取
    # detail_url = f'https://www.imdb.com/{href}'
    # response = scrape_api(detail_url)
    # if response is None:
    #     return None
    # detail_doc = pq(response.text)
    # jpg_url = detail_doc('.ipc-poster a').attr('href')  # class='.poster' <a> <img>标签下的src属性
    # return f'https://www.imdb.com/{jpg_url}'


def get_info_from_imdb():
    image_file = open("parse_files/image.csv", "a", encoding='UTF-8')
    image_file_writer = csv.writer(image_file)
    continue_flag = False
    with open("parse_files/movies_metadata.csv", "r", encoding='UTF-8') as movies:
        movies_reader = csv.reader(movies)
        next(movies_reader)

        for movie in movies_reader:
            movie_id = movie[5]
            if not continue_flag and movie_id == str(27058):
                continue_flag = True
            if continue_flag:
                try:
                    imdb_id = movie[20]
                    data = get_movie_png(imdb_id)
                    image_file_writer.writerow([movie_id, data])
                except Exception as e:
                    print(e)


def check_num(a_file, b_file):
    print("big_file_data_num: " + str(row_count("data/" + b_file + ".csv")))
    print("small_file_data_num: " + str(row_count("data/" + a_file + ".csv")))
    print("merged_data_num: " + str(row_count("parse_files/" + a_file + "_merged.csv")))


def get_poster_from_omdb(api_key, start_id="862"):
    with open("parse_files/posters.csv", "a", encoding="UTF-8") as poster_file:
        poster_file_write = csv.writer(poster_file)
        continue_flag = False
        with open("parse_files/movies_metadata.csv", "r", encoding='UTF-8') as movies:
            movies_reader = csv.reader(movies)
            next(movies_reader)

            for movie in movies_reader:
                movie_id = movie[5]
                if not continue_flag and movie_id == start_id:
                    continue_flag = True
                if continue_flag:
                    try:
                        imdb_id = movie[6]
                        if imdb_id == "":
                            continue
                        para = {"tt": imdb_id}
                        # data = requests.post("https://betterimdbot.herokuapp.com/", para)
                        data = requests.get("http://www.omdbapi.com/?apikey=" + api_key + "&i=" + imdb_id)
                        trails = 0
                        while data.status_code != 200 and trails < 10:
                            data = requests.get("http://www.omdbapi.com/?apikey=" + api_key + "&i=" + imdb_id)
                            # data = requests.post("https://betterimdbot.herokuapp.com/", para)
                            trails = trails + 1
                        print(json.loads(data.content)["Poster"])
                        # if not json.loads(data.content).__contains__("poster"):
                        #     continue
                        # print(json.loads(data.content)["poster"])
                        poster_file_write.writerow([movie_id, json.loads(data.content)["Poster"]])
                        # poster_file_write.writerow([movie_id, json.loads(data.content)["poster"]])
                    except Exception as e:
                        print(e)
                        print(movie_id)
                        return movie_id
    return None


# print("-----------------------      start data parsing      -------------------------------")


#
# parse_necessary_data()
#
# print("-----------------------  start relations generating  -------------------------------")
# generate_relations()
#
# print("-----------------------  merge two files  -----------------------------")
# merge_files()
#
# check_num("links", "links_small")
# check_num("ratings", "ratings_small")
#
# generate_user()
# print("-----------------------  start data parsing for neo4j import  -----------------------------")
# parse_necessary_data_neo4j_import()
#
# generate_relations_neo4j_import_batch()

# get_info_from_imdb()
# api_keys = ["9a439834", "f9bf98fc", "f853334d", "3868f7e6", "9062d67e", "4ef56ef0", "cccbec2e", "73b1f0ea"]
# start_id = "44333"
# index = 0
# while start_id is not None:
#     start_id = get_poster_from_omdb(api_keys[0], start_id)
#     index += 1
new_movies_file = open("parse_files/new_movies.csv", "w", encoding='UTF-8')
new_movies_file_writer = csv.writer(new_movies_file)
posters_map = {}
score_map = {}
with open("parse_files/posters.csv", "r", encoding='UTF-8') as posters:
    posters_reader = csv.reader(posters)
    next(posters_reader)
    for poster in posters_reader:
        posters_map[poster[0]] = poster[1]

with open("parse_files/avg_ratings.csv", "r", encoding='UTF-8') as score:
    score_reader = csv.reader(score)
    next(score_reader)
    for score in score_reader:
        score_map[score[1]] = score[0]

with open("parse_files/movies_metadata.csv", "r", encoding='UTF-8') as movies:
    movies_reader = csv.reader(movies)
    header = next(movies_reader)
    header.append("score")
    new_movies_file_writer.writerow(header)
    for movie in movies_reader:
        if len(movie) != 24:
            continue
        movie_id = movie[5]
        if posters_map.__contains__(movie_id):
            movie[11] = posters_map[movie_id]
        if score_map.__contains__(movie_id):
            movie.append(score_map[movie_id])
        else:
            movie.append(0)
        new_movies_file_writer.writerow(movie)
