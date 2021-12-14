package advanced.database.course.demo.service;


import java.lang.String;

import advanced.database.course.demo.entity.SpokenLanguage;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:05
 */
public interface SpokenLanguageService {

    void save(SpokenLanguage spokenLanguage);

    void deleteById(String id);

    SpokenLanguage findById(String id);

    List<SpokenLanguage> findAll();
}

