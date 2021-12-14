package advanced.database.course.demo.service.impl;


import java.lang.String;

import advanced.database.course.demo.entity.SpokenLanguage;
import advanced.database.course.demo.service.SpokenLanguageService;
import advanced.database.course.demo.repository.SpokenLanguageRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:05
 */
@Service
public class SpokenLanguageServiceImpl implements SpokenLanguageService {

    @Autowired
    private SpokenLanguageRepository spokenLanguageRepository;

    @Override
    public void save(SpokenLanguage spokenLanguage) {
        spokenLanguageRepository.save(spokenLanguage);
    }

    @Override
    public void deleteById(String id) {
        spokenLanguageRepository.deleteByIso6391(id);
    }

    @Override
    public SpokenLanguage findById(String id) {
        return spokenLanguageRepository.findOneByIso6391(id);
    }

    @Override
    public List<SpokenLanguage> findAll() {
        return spokenLanguageRepository.findAll();
    }

}

