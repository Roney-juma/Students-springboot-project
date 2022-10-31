package com.example.practice.student;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@Service
public class StudentService {
    @GetMapping
    public List<Student> getStudent(){
        return List.of(
                new Student(
                        1L,"Roney","rj@gmail.com", LocalDate.of(1998, Month.MAY,27), 24
                )
        );
    }
}
