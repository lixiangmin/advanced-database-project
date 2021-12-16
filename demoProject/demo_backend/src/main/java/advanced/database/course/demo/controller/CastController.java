package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Cast;
import advanced.database.course.demo.service.CastService;
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
 * @since 2021-12-13 12:59:58
 */
@RestController
@RequestMapping("/cast")
@AllArgsConstructor
public class CastController {

    @Autowired
    private final CastService castService;

    /**
     * 获取
     */
    @GetMapping("/get{id}")
    public Cast get(@PathVariable("id") Integer id) {
        return castService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Cast cast) {
        castService.save(cast);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Cast cast) {
        castService.save(cast);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        castService.deleteById(id);
    }

}

