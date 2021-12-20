package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:59
 */
public interface GenreService {

    void save(Genre genre);

    void deleteById(Integer id);

    Genre findById(Integer id);

    List<Genre> findAll();

    Page<Genre> findAll(Pageable var1);
}

