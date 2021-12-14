package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Keyword;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:00
 */
@Repository
public interface KeywordRepository extends JpaRepository<Keyword, Integer> {
    void deleteById(Integer id);

    Keyword findOneById(Integer id);
}

