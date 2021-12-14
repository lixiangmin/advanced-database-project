package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Cast;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:57
 */
@Repository
public interface CastRepository extends JpaRepository<Cast, Integer> {
    void deleteById(Integer id);

    Cast findOneById(Integer id);
}

