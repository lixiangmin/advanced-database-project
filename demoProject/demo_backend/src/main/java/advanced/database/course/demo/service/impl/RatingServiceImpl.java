package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Rating;
import advanced.database.course.demo.service.RatingService;
import advanced.database.course.demo.repository.RatingRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:05
 */
@Service
public class RatingServiceImpl implements RatingService {

    @Autowired
    private RatingRepository ratingRepository;

    @Override
    public void save(Rating rating) {
        ratingRepository.save(rating);
    }

    @Override
    public void deleteById(Integer id) {
        ratingRepository.deleteByRatingId(id);
    }

    @Override
    public Rating findById(Integer id) {
        return ratingRepository.findOneByRatingId(id);
    }

    @Override
    public List<Rating> findAll() {
        return ratingRepository.findAll();
    }

}

