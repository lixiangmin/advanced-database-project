package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:59
 */
@Repository
public interface GenreRepository extends JpaRepository<Genre, Integer> {
    void deleteById(Integer id);

    Genre findOneById(Integer id);
}

