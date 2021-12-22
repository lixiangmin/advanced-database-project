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

    @Autowired
    private RatingRepository ratingRepository;

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
    public List<Movie> getRecommendsById(Integer id) {
        int targetNum = 6;
        List<Rating> ratings = ratingRepository.findByMovieId(id);
        Collections.sort(ratings, (Comparator<Rating>) (o1, o2) -> o2.getRating().compareTo(o1.getRating()));
        int end = Math.min(ratings.size(), 100);
        ratings = ratings.subList(0, end);
        HashMap<Integer, Integer> maps = new HashMap<>();
        for (Rating rating : ratings) {
            List<Rating> userMovies = ratingRepository.findByUserId(rating.getUserId());
            for (Rating userMovie : userMovies) {
                int movieId = userMovie.getMovieId();
                if (maps.containsKey(movieId)) {
                    maps.put(movieId, maps.get(movieId) + 1);
                } else {
                    maps.put(movieId, 1);
                }
            }
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<Map.Entry<Integer, Integer>>(maps.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> o1,
                               Map.Entry<Integer, Integer> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });
        List<Movie> movies = new ArrayList<>();
        int index = 0;
        while (movies.size() < targetNum && index < list.size()) {
            int movieId = list.get(index).getKey();
            if (movieId == id) {
                continue;
            }
            Movie movie = movieRepository.findOneById(movieId);
            if (movie == null) {
                index += 1;
                continue;
            }
            movies.add(movie);
            index += 1;
        }
        if (movies.size() < targetNum) {
            Movie movie = movieRepository.findOneById(id);
            Set<Genre> genres = movie.getGenres();
            for (Genre genre : genres) {
                List<Movie> genreMovies = new ArrayList<>();
                genreMovies.addAll(genre.getMovies());
                Collections.shuffle(genreMovies);
                for (Movie m : genreMovies) {
                    if (id == m.getId())
                        continue;
                    movies.add(m);
                    if (movies.size() == targetNum) {
                        return movies;
                    }
                }
            }
        }
        return movies;
    }

    @Override
    public Page<Movie> searchMoviesByText(String text, Pageable pageable) {
        return movieRepository.searchMoviesByText(text, pageable);
    }

    @Override
    public Page<Movie> searchMoviesByGenreId(int genreId, Pageable pageRequest) {
        return movieRepository.searchMoviesByGenreId(genreId,pageRequest);
    }

    @Override
    public Page<Movie> searchMoviesByMovieId(int movieId, Pageable pageRequest) {
        return movieRepository.searchMoviesByMovieId(movieId,pageRequest);
    }

}

