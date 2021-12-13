package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Cast;
import advanced.database.course.demo.service.CastService;
import advanced.database.course.demo.repository.CastRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:57
 */
@Service
public class CastServiceImpl implements CastService {

    @Autowired
    private CastRepository castRepository;

    @Override
    public void save(Cast cast) {
        castRepository.save(cast);
    }

    @Override
    public void deleteById(Integer id) {
        castRepository.deleteById(id);
    }

    @Override
    public Cast findById(Integer id) {
        return castRepository.findOneById(id);
    }

    @Override
    public List<Cast> findAll() {
        return castRepository.findAll();
    }

}

