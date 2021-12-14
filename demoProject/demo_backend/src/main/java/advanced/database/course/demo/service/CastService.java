package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Cast;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:57
 */
public interface CastService {

    void save(Cast cast);

    void deleteById(Integer id);

    Cast findById(Integer id);

    List<Cast> findAll();
}

