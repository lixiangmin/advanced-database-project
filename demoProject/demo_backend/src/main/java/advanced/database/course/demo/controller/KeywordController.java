package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Keyword;
import advanced.database.course.demo.service.KeywordService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.*;

/**
 * 控制层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:01
 */
@RestController
@RequestMapping("/keyword")
@AllArgsConstructor
public class KeywordController {

    @Autowired
    private final KeywordService keywordService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Keyword get(Integer id) {
        return keywordService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Keyword keyword) {
        keywordService.save(keyword);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Keyword keyword) {
        keywordService.save(keyword);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        keywordService.deleteById(id);
    }

}

