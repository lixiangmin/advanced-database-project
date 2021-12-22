package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.Crew;
import advanced.database.course.demo.service.CrewService;
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
@RequestMapping("/api/crew")
@AllArgsConstructor
public class CrewController {

    @Autowired
    private final CrewService crewService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public Crew get(Integer id) {
        return crewService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody Crew crew) {
        crewService.save(crew);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody Crew crew) {
        crewService.save(crew);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        crewService.deleteById(id);
    }

}

