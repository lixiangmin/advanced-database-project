package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Movie;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:02
 */
@Repository
public interface MovieRepository extends JpaRepository<Movie, Integer> {
    void deleteById(Integer id);

    Movie findOneById(Integer id);
}

