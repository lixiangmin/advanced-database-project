package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Crew;
import advanced.database.course.demo.service.CrewService;
import advanced.database.course.demo.repository.CrewRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:58
 */
@Service
public class CrewServiceImpl implements CrewService {

    @Autowired
    private CrewRepository crewRepository;

    @Override
    public void save(Crew crew) {
        crewRepository.save(crew);
    }

    @Override
    public void deleteById(Integer id) {
        crewRepository.deleteById(id);
    }

    @Override
    public Crew findById(Integer id) {
        return crewRepository.findOneById(id);
    }

    @Override
    public List<Crew> findAll() {
        return crewRepository.findAll();
    }

}

