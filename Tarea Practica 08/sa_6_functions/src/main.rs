use rand::Rng;

const NUM_ELEMENTS: usize = 20;
const TEMP_MIN: f64 = 0.01;
const TEMP_MAX: f64 = 300.0;
const ALPHA: f64 = 0.8;
const K: f64 = 1.0;

fn alpine_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    funcion.iter().for_each(|&x| {
        valmax += ((x * x.to_radians().sin()) + (0.1 * x)).abs(); // El sin esta en Radianes
    });
    valmax
}

fn dixon_price_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = (funcion[0] - 1.0).powi(2);
    for i in 1..funcion.len() {
        valmax += (i as f64) * (2.0 * funcion[i].to_radians().sin() - funcion[i - 1]).powi(2);
    }
    valmax
}

fn quintic_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    funcion.iter().for_each(|&x| {
        valmax += (x.powi(5) - (3.0 * x.powi(4)) + (4.0 * x.powi(3))
            - (2.0 * x.powi(2))
            - (10.0 * x)
            - 4.0)
            .abs();
    });
    valmax
}

fn schwefel_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    funcion.iter().for_each(|&x| {
        valmax += x.powi(10);
    });
    valmax
}

fn streched_v_sine_wave_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    for i in 0..(funcion.len() - 1) {
        valmax += (funcion[i + 1].powi(2) + funcion[i].powi(2)).powf(0.25)
            * ((50.0 * (funcion[i + 1].powi(2) + funcion[i].powi(2)).powf(0.1))
                .to_radians()
                .sin()
                .powi(2)
                + 0.1);
    }
    valmax
}

fn sum_squares_cost(funcion: &[f64]) -> f64 {
    let mut valmax: f64 = 0.0;
    funcion.iter().enumerate().for_each(|(i, &x)| {
        valmax += (i as f64) * x.powi(2);
    });
    valmax
}

fn vecindad(funcion: &[f64]) -> Vec<f64> {
    let mut vecindad: Vec<f64> = funcion.to_vec();
    let locus = rand::thread_rng().gen_range(0..vecindad.len());
    vecindad[locus] = rand::thread_rng().gen_range(-10.0..=10.0);
    vecindad
}

fn simulated_annealing() {
    let mut funcion_x: Vec<f64> = Vec::with_capacity(NUM_ELEMENTS);
    for _ in 0..NUM_ELEMENTS {
        funcion_x.push(rand::thread_rng().gen_range(-10.0..=10.0));
    }
    let mut edo_anterior: f64 = alpine_cost(&funcion_x);

    let mut temp: f64 = TEMP_MAX;
    let vecinos: usize = funcion_x.len() - 1;

    println!("{edo_anterior}");

    while temp >= TEMP_MIN {
        let mut vecinos_revisados: usize = 0;
        while vecinos_revisados < vecinos {
            let sucesor: Vec<f64> = vecindad(&funcion_x);
            let edo_nuevo: f64 = alpine_cost(&sucesor);
            let delta = edo_nuevo - edo_anterior;
            if delta > 0.0 {
                if rand::thread_rng().gen_range(0.0..1.0) < (-delta / (K * temp)).exp() {
                    edo_anterior = edo_nuevo;
                    funcion_x = sucesor;
                }
            } else {
                edo_anterior = edo_nuevo;
                funcion_x = sucesor;
            }
            vecinos_revisados += 1;
        }
        temp *= ALPHA;
    }
    println!("{edo_anterior}");
}

fn main() {
    simulated_annealing();
}
