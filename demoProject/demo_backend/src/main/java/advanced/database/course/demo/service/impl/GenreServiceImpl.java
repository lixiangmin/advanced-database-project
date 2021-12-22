package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.Genre;
import advanced.database.course.demo.service.GenreService;
import advanced.database.course.demo.repository.GenreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 12:59:59
 */
@Service
public class GenreServiceImpl implements GenreService {

    @Autowired
    private GenreRepository genreRepository;

    @Override
    public void save(Genre genre) {
        genreRepository.save(genre);
    }

    @Override
    public void deleteById(Integer id) {
        genreRepository.deleteById(id);
    }

    @Override
    public Genre findById(Integer id) {
        return genreRepository.findOneById(id);
    }

    @Override
    public Genre findByName(String name) {
        return genreRepository.findByName(name);
    }

    @Override
    public List<Genre> findAll() {
        return genreRepository.findAll();
    }

    @Override
    public Page<Genre> findAll(Pageable var1) {
        return genreRepository.findAll(var1);
    }
}

