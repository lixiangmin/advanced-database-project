package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Link;
import advanced.database.course.demo.service.LinkService;
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
 * @since 2021-12-13 13:00:02
 */
@RestController
@RequestMapping("/link")
@AllArgsConstructor
public class LinkController {

    @Autowired
    private final LinkService linkService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Link get(Integer id) {
        return linkService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Link link) {
        linkService.save(link);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Link link) {
        linkService.save(link);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        linkService.deleteById(id);
    }

}

