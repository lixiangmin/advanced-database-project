package advanced.database.course.demo.controller;


import java.lang.Integer;
import java.util.HashMap;
import java.util.Map;

import advanced.database.course.demo.entity.User;
import advanced.database.course.demo.service.UserService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.*;

/**
 * 控制层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:07
 */
@RestController
@CrossOrigin
@RequestMapping("/api/user")
@AllArgsConstructor
public class UserController {

    @Autowired
    private final UserService userService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public User get(Integer id) {
        return userService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody User user) {
        userService.save(user);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody User user) {
        userService.save(user);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        userService.deleteById(id);
    }


    @PostMapping("login")
    public ResponseEntity<?> login(String username) {
        boolean bool = userService.login(username);
        Map<Object, Object> result = new HashMap<>();
        if (bool) {
            result.put("msg", "Success");
            result.put("code", 0);
        } else {
            result.put("code", 404);
            result.put("msg", "Username Not Found");
        }
        return new ResponseEntity<>(result, HttpStatus.OK);
    }
}

