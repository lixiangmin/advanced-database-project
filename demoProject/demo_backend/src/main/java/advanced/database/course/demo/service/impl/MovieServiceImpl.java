package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.entity.Rating;
import advanced.database.course.demo.repository.RatingRepository;
import advanced.database.course.demo.service.MovieService;
import advanced.database.course.demo.repository.MovieRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.*;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:02
 */
@Service
public class MovieServiceImpl implements MovieService {

    @Autowired
    private MovieRepository movieRepository;

    @Override
    public void save(Movie movie) {
        movieRepository.save(movie);
    }

    @Override
    public void deleteById(Integer id) {
        movieRepository.deleteById(id);
    }

    @Override
    public Movie findById(Integer id) {
        return movieRepository.findOneById(id);
    }

    @Override
    public List<Movie> findAll() {
        return movieRepository.findAll();
    }

    @Override
    public Page<Movie> findAll(Pageable var1) {
        return movieRepository.findAll(var1);
    }

    @Override
    public List<Movie> findRecommendMovies() {
        return movieRepository.findRecommendMovies();
    }

    @Override
    public Page<Movie> searchMoviesByText(String text, Pageable pageable) {
        return movieRepository.searchMoviesByText(text, pageable);
    }

    @Override
    public Page<Movie> searchMoviesByGenreId(int genreId, Pageable pageRequest) {
        return movieRepository.searchMoviesByGenreId(genreId, pageRequest);
    }

    @Override
    public Page<Movie> searchMoviesByMovieId(int movieId, Pageable pageRequest) {
        Page<Movie> page = movieRepository.searchMoviesByMovieId(movieId, pageRequest);
        if (page.getTotalElements() == 0) {
            Movie movie = movieRepository.findOneById(movieId);
            Set<Genre> genres = movie.getGenres();
            if (genres.size() > 0) {
                List<Genre> genreList = new ArrayList<>();
                genreList.addAll(genres);
                return movieRepository.searchMoviesByGenreId(genreList.get(0).getId(), pageRequest);
            }
        }
        return page;
    }

}

