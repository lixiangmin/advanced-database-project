package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Keyword;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:00
 */
public interface KeywordService {

    void save(Keyword keyword);

    void deleteById(Integer id);

    Keyword findById(Integer id);

    List<Keyword> findAll();
}

