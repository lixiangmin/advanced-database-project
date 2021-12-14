package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Link;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:01
 */
public interface LinkService {

    void save(Link link);

    void deleteById(Integer id);

    Link findById(Integer id);

    List<Link> findAll();
}

