package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.service.GenreService;
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
 * @since 2021-12-13 12:59:59
 */
@RestController
@RequestMapping("/genre")
@AllArgsConstructor
public class GenreController {

    @Autowired
    private final GenreService genreService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Genre get(Integer id) {
        return genreService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Genre genre) {
        genreService.save(genre);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Genre genre) {
        genreService.save(genre);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        genreService.deleteById(id);
    }

}

