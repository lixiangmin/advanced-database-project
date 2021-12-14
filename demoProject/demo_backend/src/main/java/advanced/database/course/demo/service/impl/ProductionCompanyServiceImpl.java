package advanced.database.course.demo.service.impl;


import java.lang.Integer;

import advanced.database.course.demo.entity.ProductionCompany;
import advanced.database.course.demo.service.ProductionCompanyService;
import advanced.database.course.demo.repository.ProductionCompanyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:03
 */
@Service
public class ProductionCompanyServiceImpl implements ProductionCompanyService {

    @Autowired
    private ProductionCompanyRepository productionCompanyRepository;

    @Override
    public void save(ProductionCompany productionCompany) {
        productionCompanyRepository.save(productionCompany);
    }

    @Override
    public void deleteById(Integer id) {
        productionCompanyRepository.deleteById(id);
    }

    @Override
    public ProductionCompany findById(Integer id) {
        return productionCompanyRepository.findOneById(id);
    }

    @Override
    public List<ProductionCompany> findAll() {
        return productionCompanyRepository.findAll();
    }

}

