package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Rating;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:05
 */
@Repository
public interface RatingRepository extends JpaRepository<Rating, Integer> {
    void deleteByRatingId(Integer id);

    Rating findOneByRatingId(Integer id);
}

