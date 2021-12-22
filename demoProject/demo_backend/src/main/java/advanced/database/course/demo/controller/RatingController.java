package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Rating;
import advanced.database.course.demo.service.RatingService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.*;

/**
 * 控制层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:05
 */
@RestController
@RequestMapping("/api/rating")
@AllArgsConstructor
public class RatingController {

    @Autowired
    private final RatingService ratingService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Rating get(Integer id) {
        return ratingService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Rating rating) {
        ratingService.save(rating);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Rating rating) {
        ratingService.save(rating);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        ratingService.deleteById(id);
    }

}

