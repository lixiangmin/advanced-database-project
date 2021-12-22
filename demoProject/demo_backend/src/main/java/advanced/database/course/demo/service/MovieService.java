package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.entity.Movie;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:02
 */
public interface MovieService {

    void save(Movie movie);

    void deleteById(Integer id);

    Movie findById(Integer id);

    List<Movie> findAll();

    Page<Movie> findAll(Pageable var1);

    List<Movie> findRecommendMovies();

    Page<Movie> searchMoviesByText(String text, Pageable pageRequest);

    Page<Movie> searchMoviesByGenreId(int type, Pageable pageRequest);

    Page<Movie> searchMoviesByMovieId(int movieId, Pageable pageRequest);
}

