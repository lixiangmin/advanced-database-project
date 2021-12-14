package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Rating;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:04
 */
public interface RatingService {

    void save(Rating rating);

    void deleteById(Integer id);

    Rating findById(Integer id);

    List<Rating> findAll();
}

