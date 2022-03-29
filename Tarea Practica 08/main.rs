use std::vec;

fn alpine_fitness(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    funcion.iter().for_each(|&x| {
        valmax += ((x * x.to_radians().sin()) + (0.1 * x)).abs(); // El sin esta en Radianes
    });
    valmax
}

fn dixon_fitness(funcion: &[f64]) -> f64 {
    todo!();
}

fn quintic_fitness(funcion: &[f64]) -> f64 {
    todo!();
}

fn schwefel_fitness(funcion: &[f64]) -> f64 {
    todo!();
}

fn streched_v_sine_wave_fitness(funcion: &[f64]) -> f64 {
    todo!();
}

fn sum_squares_fitness(funcion: &[f64]) -> f64 {
    todo!();
}

fn main() {
    let valores: Vec<f64> = vec![0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0];
    println!("{}", valores[3].to_radians().sin());
}
