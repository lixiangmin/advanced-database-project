package advanced.database.course.demo.service.impl;


import java.lang.String;

import advanced.database.course.demo.entity.ProductionCountry;
import advanced.database.course.demo.service.ProductionCountryService;
import advanced.database.course.demo.repository.ProductionCountryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:04
 */
@Service
public class ProductionCountryServiceImpl implements ProductionCountryService {

    @Autowired
    private ProductionCountryRepository productionCountryRepository;

    @Override
    public void save(ProductionCountry productionCountry) {
        productionCountryRepository.save(productionCountry);
    }

    @Override
    public void deleteById(String id) {
        productionCountryRepository.deleteByIso31661(id);
    }

    @Override
    public ProductionCountry findById(String id) {
        return productionCountryRepository.findOneByIso31661(id);
    }

    @Override
    public List<ProductionCountry> findAll() {
        return productionCountryRepository.findAll();
    }

}

