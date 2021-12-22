package advanced.database.course.demo.controller;


import java.lang.Integer;
import java.util.*;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.service.GenreService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
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
@RequestMapping("/api/genre")
@AllArgsConstructor
@CrossOrigin
public class GenreController {

    @Autowired
    private final GenreService genreService;

    /**
     * 获取
     */
    @GetMapping("/get/{id}")
    public Genre get(@PathVariable("id") Integer id) {
        return genreService.findById(id);
    }

    /**
     * 全部获取
     */
    @GetMapping("")
    public ResponseEntity<?> findAll() {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("genres", genreService.findAll());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    /**
     * 分页获取
     */
    @GetMapping("/page")
    public List<Genre> findAll(Pageable var1) {
        Pageable pageRequest = PageRequest.of(0, 5);
        Page<Genre> page = genreService.findAll(pageRequest);
        return page.getContent();
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

    @GetMapping("/getMovies")
    public ResponseEntity<?> getMovies(@RequestParam("type") String type) {
        Map<Object, Object> result = new HashMap<>();
        List<Movie> movies = new ArrayList<>();
        Genre genre = genreService.findByName(type);
        movies.addAll(genre.getMovies());
        Collections.sort(movies, new Comparator<Movie>() {
            @Override
            public int compare(Movie o1, Movie o2) {
                if (o1.getScore() > o2.getScore()) {
                    return -1;
                } else if (o1.getScore().equals(o2.getScore())) {
                    return 0;
                } else return 1;
            }
        });
        result.put("msg", "Success");
        result.put("movies", movies.subList(0,6));
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

}

