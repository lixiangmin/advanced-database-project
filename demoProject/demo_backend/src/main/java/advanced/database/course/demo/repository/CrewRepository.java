package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Crew;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:58
 */
@Repository
public interface CrewRepository extends JpaRepository<Crew, Integer> {
    void deleteById(Integer id);

    Crew findOneById(Integer id);
}

