package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.entity.Movie;
import advanced.database.course.demo.service.MovieService;
import advanced.database.course.demo.repository.MovieRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;


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

}

