package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Crew;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:58
 */
public interface CrewService {

    void save(Crew crew);

    void deleteById(Integer id);

    Crew findById(Integer id);

    List<Crew> findAll();
}

