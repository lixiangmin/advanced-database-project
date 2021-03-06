package advanced.database.course.demo.controller;


import java.lang.Integer;

import advanced.database.course.demo.entity.ProductionCompany;
import advanced.database.course.demo.service.ProductionCompanyService;
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
 * @since 2021-12-13 13:00:03
 */
@RestController
@RequestMapping("/api/productionCompany")
@AllArgsConstructor
public class ProductionCompanyController {

    @Autowired
    private final ProductionCompanyService productionCompanyService;

    /**
     * 获取
     */
    @GetMapping("/get")
    public ProductionCompany get(Integer id) {
        return productionCompanyService.findById(id);
    }

    /**
     * 添加
     */
    @PostMapping("/add")
    public void add(@RequestBody ProductionCompany productionCompany) {
        productionCompanyService.save(productionCompany);
    }


    /**
     * 修改
     */
    @PostMapping("/update")
    public void update(@RequestBody ProductionCompany productionCompany) {
        productionCompanyService.save(productionCompany);
    }

    /**
     * 删除
     */
    @PostMapping("/delete")
    public void delete(Integer id) {
        productionCompanyService.deleteById(id);
    }

}

