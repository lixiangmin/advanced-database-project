package advanced.database.course.demo.controller;


import java.lang.String;

import advanced.database.course.demo.entity.ProductionCountry;
import advanced.database.course.demo.service.ProductionCountryService;
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
 * @since 2021-12-13 13:00:04
 */
@RestController
@RequestMapping("/api/productionCountry")
@AllArgsConstructor
public class ProductionCountryController {

    @Autowired
    private final ProductionCountryService productionCountryService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public ProductionCountry get(String id) {
        return productionCountryService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody ProductionCountry productionCountry) {
        productionCountryService.save(productionCountry);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody ProductionCountry productionCountry) {
        productionCountryService.save(productionCountry);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(String id) {
        productionCountryService.deleteById(id);
    }

}

