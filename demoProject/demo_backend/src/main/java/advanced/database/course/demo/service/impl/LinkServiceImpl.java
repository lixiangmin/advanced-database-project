package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Link;
import advanced.database.course.demo.service.LinkService;
import advanced.database.course.demo.repository.LinkRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:01
 */
@Service
public class LinkServiceImpl implements LinkService {

    @Autowired
    private LinkRepository linkRepository;

    @Override
    public void save(Link link) {
        linkRepository.save(link);
    }

    @Override
    public void deleteById(Integer id) {
        linkRepository.deleteById(id);
    }

    @Override
    public Link findById(Integer id) {
        return linkRepository.findOneById(id);
    }

    @Override
    public List<Link> findAll() {
        return linkRepository.findAll();
    }

}

