package advanced.database.course.demo.controller;


import java.lang.Integer;
import java.util.HashMap;
import java.util.Map;

import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.service.MovieService;
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
 * @since 2021-12-13 13:00:02
 */
@RestController
@RequestMapping("/api/movie")
@AllArgsConstructor
@CrossOrigin
public class MovieController {

    @Autowired
    private final MovieService movieService;

    @GetMapping("/recommend/{id}")
    public ResponseEntity<?> getRecommends(@PathVariable Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("recommends", movieService.getRecommendsById(id));
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    /**
     * 按id获取
     *
     * @param id，对应电影的id
     */
    @GetMapping("/{id}")
    public ResponseEntity<?> get(@PathVariable Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movie", movieService.findById(id));
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    /**
     * 分页获取
     *
     * @param page，页码，或叫offset
     * @param size，每页大小，或叫count
     */
    @GetMapping("/list")
    public ResponseEntity<?> findAll(@RequestParam("page") int page, @RequestParam("size") int size) {
        Pageable pageRequest = PageRequest.of(page, size);
        Page<Movie> resultPage = movieService.findAll(pageRequest);
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movies", resultPage.getContent());
        result.put("total", resultPage.getTotalElements());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/searchByText")
    public ResponseEntity<?> searchMoviesByText(@RequestParam("text") String text, @RequestParam("page") int page, @RequestParam("size") int size) {
        Pageable pageRequest = PageRequest.of(page, size);
        Page<Movie> resultPage = movieService.searchMoviesByText(text, pageRequest);
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movies", resultPage.getContent());
        result.put("total", resultPage.getTotalElements());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/searchByGenreId")
    public ResponseEntity<?> searchMoviesByGenreId(@RequestParam("genreId") int genreId, @RequestParam("page") int page, @RequestParam("size") int size) {
        Pageable pageRequest = PageRequest.of(page, size);
        Page<Movie> resultPage = movieService.searchMoviesByGenreId(genreId, pageRequest);
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movies", resultPage.getContent());
        result.put("total", resultPage.getTotalElements());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/searchByMovieId")
    public ResponseEntity<?> searchMoviesByMovieId(@RequestParam("movieId") int movieId, @RequestParam("page") int page, @RequestParam("size") int size) {
        Pageable pageRequest = PageRequest.of(page, size);
        Page<Movie> resultPage = movieService.searchMoviesByMovieId(movieId, pageRequest);
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movies", resultPage.getContent());
        result.put("total", resultPage.getTotalElements());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
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

    @GetMapping("/recommend/movies")
    public ResponseEntity<?> getRecommendMovies() {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        result.put("movies", movieService.findRecommendMovies());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/getTypes")
    public ResponseEntity<?> getTypes(@RequestParam("id") Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        Movie movie = movieService.findById(id);
        result.put("types", movie.getGenres());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }
    @GetMapping("/getKeywords")
    public ResponseEntity<?> getKeywords(@RequestParam("id") Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        Movie movie = movieService.findById(id);
        result.put("keywords", movie.getKeywords());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/getCrews")
    public ResponseEntity<?> getCrews(@RequestParam("id") Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        Movie movie = movieService.findById(id);
        result.put("crews", movie.getCrews());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    @GetMapping("/getCasts")
    public ResponseEntity<?> getCasts(@RequestParam("id") Integer id) {
        Map<Object, Object> result = new HashMap<>();
        result.put("msg", "Success");
        Movie movie = movieService.findById(id);
        result.put("casts", movie.getCasts());
        result.put("code", 0);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

}

