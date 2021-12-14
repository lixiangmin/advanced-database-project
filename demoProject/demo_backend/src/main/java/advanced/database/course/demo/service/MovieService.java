package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Movie;

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
}

