package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.User;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:06
 */
public interface UserService {

    void save(User user);

    void deleteById(Integer id);

    User findById(Integer id);

    List<User> findAll();

    boolean login(String username);
}

