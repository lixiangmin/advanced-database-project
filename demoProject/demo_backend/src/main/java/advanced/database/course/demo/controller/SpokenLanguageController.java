package advanced.database.course.demo.controller;


import java.lang.String;

import advanced.database.course.demo.entity.SpokenLanguage;
import advanced.database.course.demo.service.SpokenLanguageService;
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
 * @since 2021-12-13 13:00:06
 */
@RestController
@RequestMapping("/api/spokenLanguage")
@AllArgsConstructor
public class SpokenLanguageController {

    @Autowired
    private final SpokenLanguageService spokenLanguageService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public SpokenLanguage get(String id) {
        return spokenLanguageService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody SpokenLanguage spokenLanguage) {
        spokenLanguageService.save(spokenLanguage);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody SpokenLanguage spokenLanguage) {
        spokenLanguageService.save(spokenLanguage);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(String id) {
        spokenLanguageService.deleteById(id);
    }

}

