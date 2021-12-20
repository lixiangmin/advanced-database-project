package advanced.database.course.demo.controller;


import java.lang.Integer;
import java.util.List;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.service.MovieService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
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
     * 按id获取
     * @param id，对应电影的id
     */
    @GetMapping("/recommend/{id}")
    public Movie get(@PathVariable Integer id) {
        return movieService.findById(id);
    }

    /**
     * 分页获取
     * @param page，页码，或叫offset
     * @param size，每页大小，或叫count
     */
    @GetMapping("/list/{page}/{size}")
    public List<Movie> findAll(@PathVariable("page") int page,@PathVariable("size") int size) {

        Pageable pageRequest= PageRequest.of(page,size);
        Page<Movie> resultPage=movieService.findAll(pageRequest);
        return resultPage.getContent();
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

