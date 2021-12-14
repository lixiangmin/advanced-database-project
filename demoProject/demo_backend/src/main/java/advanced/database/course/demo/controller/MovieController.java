package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.service.MovieService;
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
 * @since 2021-12-13 13:00:02
 */
@RestController
@RequestMapping("/movie")
@AllArgsConstructor
public class MovieController {

    @Autowired
    private final MovieService movieService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Movie get(Integer id) {
        return movieService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Movie movie) {
        movieService.save(movie);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Movie movie) {
        movieService.save(movie);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        movieService.deleteById(id);
    }

}

