package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.User;
import advanced.database.course.demo.service.UserService;
import advanced.database.course.demo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:06
 */
@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public void save(User user) {
        userRepository.save(user);
    }

    @Override
    public void deleteById(Integer id) {
        userRepository.deleteById(id);
    }

    @Override
    public User findById(Integer id) {
        return userRepository.findOneById(id);
    }

    @Override
    public List<User> findAll() {
        return userRepository.findAll();
    }

    @Override
    public boolean login(String username) {
        return userRepository.findOneByName(username) != null;
    }

}

