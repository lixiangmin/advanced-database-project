package advanced.database.course.demo.repository;


import java.lang.String;

import advanced.database.course.demo.entity.SpokenLanguage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:06
 */
@Repository
public interface SpokenLanguageRepository extends JpaRepository<SpokenLanguage, String> {
    void deleteByIso6391(String id);

    SpokenLanguage findOneByIso6391(String id);
}

