package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Keyword;
import advanced.database.course.demo.service.KeywordService;
import advanced.database.course.demo.repository.KeywordRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:00
 */
@Service
public class KeywordServiceImpl implements KeywordService {

    @Autowired
    private KeywordRepository keywordRepository;

    @Override
    public void save(Keyword keyword) {
        keywordRepository.save(keyword);
    }

    @Override
    public void deleteById(Integer id) {
        keywordRepository.deleteById(id);
    }

    @Override
    public Keyword findById(Integer id) {
        return keywordRepository.findOneById(id);
    }

    @Override
    public List<Keyword> findAll() {
        return keywordRepository.findAll();
    }

}

