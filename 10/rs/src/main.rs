use glium::Surface;
use glium::glutin;
use glium::implement_vertex;
use glium::uniform;
use std::f32;
use std::borrow::Cow;
use glium::{
    texture::{ClientFormat, RawImage2d},
};

#[derive(Debug)]
struct State {
    pan: (f64, f64),
    panning: bool,
}

fn main() {
    let mut events_loop = glutin::EventsLoop::new();
    let window = glutin::WindowBuilder::new();
    let context = glutin::ContextBuilder::new();
    let display = glium::Display::new(window, context, &events_loop).unwrap();

    #[derive(Copy, Clone)]
    struct Vertex {
        position: [f32; 2],
        tex_coords: [f32; 2],
    }

    implement_vertex!(Vertex, position, tex_coords);

    let vertex1 = Vertex { position: [-1.0, -1.0], tex_coords: [0.0, 0.0] };
    let vertex2 = Vertex { position: [-1.0,  1.0], tex_coords: [0.0, 1.0] };
    let vertex3 = Vertex { position: [ 1.0, -1.0], tex_coords: [1.0, 0.0] };

    let vertex4 = Vertex { position: [ 1.0,  1.0], tex_coords: [1.0, 1.0] };
    let vertex5 = Vertex { position: [-1.0,  1.0], tex_coords: [0.0, 1.0] };
    let vertex6 = Vertex { position: [ 1.0, -1.0], tex_coords: [1.0, 0.0] };

    let shape = vec![vertex1, vertex2, vertex3, vertex4, vertex5, vertex6];

    let vertex_buffer = glium::VertexBuffer::new(&display, &shape).unwrap();
    let indices = glium::index::NoIndices(glium::index::PrimitiveType::TrianglesList);

    let vertex_shader_src = r#"
        #version 430
        in vec2 position;
        in vec2 tex_coords;
        out vec2 v_tex_coords;
        uniform mat4 matrix;
        void main() {
            v_tex_coords = tex_coords;
            gl_Position = matrix * vec4(position, 0.0, 1.0);
        }
    "#;

    let fragment_shader_src = r#"
        #version 430
        in vec2 v_tex_coords;
        out vec4 color;
        uniform sampler2D tex;
        void main() {
            color = texture(tex, v_tex_coords);
        }
    "#;

    let program = glium::Program::from_source(&display, vertex_shader_src, fragment_shader_src, None).unwrap();

    let mut t : f32 = 0.0;
            
    let mut closed = false;
    while !closed {

        t += 1.0;

        let texture;
        {
            let w = 640;
            let h = 480;

            let mut data = Vec::with_capacity(w * h);
            for i in 0..w {
                for j in 0..h {
                    // Insert RGB values
                    if i%10 == 0 || i%10 == 1 {
                        data.push(1);
                        data.push(1);
                        data.push(1);
                    } else {
                        data.push(i as u8);
                        data.push(j as u8);
                        data.push((i + j) as u8);
                    }
                }
            }

            let raw = RawImage2d {
                data: Cow::Borrowed(&data),
                width: w as u32,
                height: h as u32,
                format: ClientFormat::U8U8U8,
            };
            texture = glium::texture::Texture2d::new(&display, raw).unwrap();
        }

        let mut target = display.draw();
        target.clear_color(
            0.5 + 0.1*(0.05 * t).sin(),
            0.5 + 0.1*(0.10 * t).sin(), 
            0.5 + 0.1*(0.15 * t).sin(), 1.0);

        let uniforms = uniform! {
            matrix: [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0f32],
            ],
            tex: &texture,
        };

        target.draw(&vertex_buffer, &indices, &program, &uniforms, &Default::default()).unwrap();

        target.finish().unwrap();

        events_loop.poll_events(|ev| {
            match ev {
                glutin::Event::WindowEvent { event, .. } => match event {
                    glutin::WindowEvent::CloseRequested => closed = true,
                    _ => (),
                },
                _ => (),
            }
        });
    }
}
