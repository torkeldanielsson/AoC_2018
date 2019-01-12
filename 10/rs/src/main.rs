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
struct Entry {
    start_x: i64,
    start_y: i64,
    speed_x: i64,
    speed_y: i64,
}

fn main() {

    let mut entries = Vec::new();

    entries.push(Entry{start_x: -10351, start_y: -10360, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x:  52528, start_y:  31539, speed_x: -5, speed_y: -3});
    entries.push(Entry{start_x: -31270, start_y: -20838, speed_x:  3, speed_y:  2});
    entries.push(Entry{start_x:  52486, start_y: -10365, speed_x: -5, speed_y:  1});
    entries.push(Entry{start_x:  31558, start_y:  10589, speed_x: -3, speed_y: -1});
    entries.push(Entry{start_x: -52253, start_y:  21064, speed_x:  5, speed_y: -2});
    entries.push(Entry{start_x: -10354, start_y:  42015, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x: -41798, start_y:  42013, speed_x:  4, speed_y: -4});
    entries.push(Entry{start_x: -52253, start_y: -52267, speed_x:  5, speed_y:  5});
    entries.push(Entry{start_x:  31550, start_y: -41793, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x: -31290, start_y:  10591, speed_x:  3, speed_y: -1});
    entries.push(Entry{start_x:  31542, start_y: -10363, speed_x: -3, speed_y:  1});
    entries.push(Entry{start_x:  21117, start_y:  52487, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x:  21074, start_y: -41796, speed_x: -2, speed_y:  4});
    entries.push(Entry{start_x:  10619, start_y: -20840, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x:  31562, start_y:  52495, speed_x: -3, speed_y: -5});
    entries.push(Entry{start_x:  31586, start_y: -20844, speed_x: -3, speed_y:  2});
    entries.push(Entry{start_x: -20837, start_y:  42020, speed_x:  2, speed_y: -4});
    entries.push(Entry{start_x:  52486, start_y:  10589, speed_x: -5, speed_y: -1});
    entries.push(Entry{start_x:  52518, start_y: -31313, speed_x: -5, speed_y:  3});
    entries.push(Entry{start_x: -31286, start_y:  21063, speed_x:  3, speed_y: -2});
    entries.push(Entry{start_x:  31536, start_y: -41793, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x:  52523, start_y: -52268, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x: -20830, start_y: -10364, speed_x:  2, speed_y:  1});
    entries.push(Entry{start_x:  31568, start_y:  10587, speed_x: -3, speed_y: -1});
    entries.push(Entry{start_x:  21116, start_y: -10369, speed_x: -2, speed_y:  1});
    entries.push(Entry{start_x:  31558, start_y:  21060, speed_x: -3, speed_y: -2});
    entries.push(Entry{start_x:  21074, start_y:  42013, speed_x: -2, speed_y: -4});
    entries.push(Entry{start_x:  21114, start_y:  42015, speed_x: -2, speed_y: -4});
    entries.push(Entry{start_x: -52231, start_y: -52269, speed_x:  5, speed_y:  5});
    entries.push(Entry{start_x: -20819, start_y:  21064, speed_x:  2, speed_y: -2});
    entries.push(Entry{start_x:  42062, start_y: -10365, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x: -31271, start_y:  52496, speed_x:  3, speed_y: -5});
    entries.push(Entry{start_x:  10598, start_y: -41791, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x:  42038, start_y: -10361, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x:  42047, start_y: -52273, speed_x: -4, speed_y:  5});
    entries.push(Entry{start_x: -31290, start_y:  10591, speed_x:  3, speed_y: -1});
    entries.push(Entry{start_x: -41742, start_y:  21066, speed_x:  4, speed_y: -2});
    entries.push(Entry{start_x:  31590, start_y: -41790, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x: -31314, start_y: -10360, speed_x:  3, speed_y:  1});
    entries.push(Entry{start_x:  42011, start_y:  42011, speed_x: -4, speed_y: -4});
    entries.push(Entry{start_x: -10366, start_y:  10583, speed_x:  1, speed_y: -1});
    entries.push(Entry{start_x: -10349, start_y: -20844, speed_x:  1, speed_y:  2});
    entries.push(Entry{start_x: -20806, start_y: -41790, speed_x:  2, speed_y:  4});
    entries.push(Entry{start_x:  42018, start_y:  52494, speed_x: -4, speed_y: -5});
    entries.push(Entry{start_x: -41746, start_y: -52271, speed_x:  4, speed_y:  5});
    entries.push(Entry{start_x:  52507, start_y:  10590, speed_x: -5, speed_y: -1});
    entries.push(Entry{start_x: -20793, start_y:  52487, speed_x:  2, speed_y: -5});
    entries.push(Entry{start_x:  21106, start_y:  21067, speed_x: -2, speed_y: -2});
    entries.push(Entry{start_x:  42047, start_y:  21063, speed_x: -4, speed_y: -2});
    entries.push(Entry{start_x: -20794, start_y: -31321, speed_x:  2, speed_y:  3});
    entries.push(Entry{start_x:  10611, start_y: -20838, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x: -41742, start_y: -41793, speed_x:  4, speed_y:  4});
    entries.push(Entry{start_x: -41747, start_y: -31321, speed_x:  4, speed_y:  3});
    entries.push(Entry{start_x: -20838, start_y: -10367, speed_x:  2, speed_y:  1});
    entries.push(Entry{start_x: -52274, start_y: -31314, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x:  52526, start_y: -20841, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x:  21066, start_y:  42017, speed_x: -2, speed_y: -4});
    entries.push(Entry{start_x: -10354, start_y: -41789, speed_x:  1, speed_y:  4});
    entries.push(Entry{start_x: -10326, start_y:  31535, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x:  42062, start_y: -20837, speed_x: -4, speed_y:  2});
    entries.push(Entry{start_x: -10346, start_y:  31539, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x:  21090, start_y:  52494, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x: -20829, start_y: -41797, speed_x:  2, speed_y:  4});
    entries.push(Entry{start_x:  21077, start_y:  21068, speed_x: -2, speed_y: -2});
    entries.push(Entry{start_x: -20814, start_y: -20845, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x:  21103, start_y: -10366, speed_x: -2, speed_y:  1});
    entries.push(Entry{start_x: -52250, start_y: -52266, speed_x:  5, speed_y:  5});
    entries.push(Entry{start_x: -10341, start_y:  31537, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x:  10603, start_y: -20839, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x: -41782, start_y: -20839, speed_x:  4, speed_y:  2});
    entries.push(Entry{start_x: -52226, start_y: -41790, speed_x:  5, speed_y:  4});
    entries.push(Entry{start_x:  31586, start_y: -41791, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x: -20790, start_y:  31543, speed_x:  2, speed_y: -3});
    entries.push(Entry{start_x:  31575, start_y: -41793, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x:  52490, start_y:  42011, speed_x: -5, speed_y: -4});
    entries.push(Entry{start_x: -41741, start_y:  31535, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x: -10318, start_y: -31316, speed_x:  1, speed_y:  3});
    entries.push(Entry{start_x:  10585, start_y: -10369, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x:  10606, start_y:  10591, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x:  52510, start_y:  31544, speed_x: -5, speed_y: -3});
    entries.push(Entry{start_x: -20846, start_y: -20840, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x:  21058, start_y:  52490, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x: -10367, start_y: -31321, speed_x:  1, speed_y:  3});
    entries.push(Entry{start_x: -41774, start_y:  21062, speed_x:  4, speed_y: -2});
    entries.push(Entry{start_x: -52254, start_y:  52492, speed_x:  5, speed_y: -5});
    entries.push(Entry{start_x:  10640, start_y: -10360, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x: -20846, start_y: -20839, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x: -10341, start_y: -52272, speed_x:  1, speed_y:  5});
    entries.push(Entry{start_x: -10330, start_y: -10363, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x: -10353, start_y: -41797, speed_x:  1, speed_y:  4});
    entries.push(Entry{start_x: -41782, start_y:  52494, speed_x:  4, speed_y: -5});
    entries.push(Entry{start_x: -41761, start_y:  10584, speed_x:  4, speed_y: -1});
    entries.push(Entry{start_x:  42018, start_y: -10369, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x: -10365, start_y:  42014, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x: -10318, start_y:  42018, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x: -52242, start_y: -31315, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x:  21095, start_y: -20838, speed_x: -2, speed_y:  2});
    entries.push(Entry{start_x:  21058, start_y: -10368, speed_x: -2, speed_y:  1});
    entries.push(Entry{start_x: -31282, start_y:  10584, speed_x:  3, speed_y: -1});
    entries.push(Entry{start_x: -31322, start_y: -31321, speed_x:  3, speed_y:  3});
    entries.push(Entry{start_x:  21117, start_y: -52273, speed_x: -2, speed_y:  5});
    entries.push(Entry{start_x:  31543, start_y:  52496, speed_x: -3, speed_y: -5});
    entries.push(Entry{start_x:  52538, start_y:  21066, speed_x: -5, speed_y: -2});
    entries.push(Entry{start_x:  10582, start_y:  52492, speed_x: -1, speed_y: -5});
    entries.push(Entry{start_x: -41777, start_y: -52265, speed_x:  4, speed_y:  5});
    entries.push(Entry{start_x: -10357, start_y: -52264, speed_x:  1, speed_y:  5});
    entries.push(Entry{start_x:  42053, start_y:  31535, speed_x: -4, speed_y: -3});
    entries.push(Entry{start_x:  42028, start_y: -20845, speed_x: -4, speed_y:  2});
    entries.push(Entry{start_x: -10326, start_y: -20845, speed_x:  1, speed_y:  2});
    entries.push(Entry{start_x:  10638, start_y:  10585, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x:  31591, start_y:  42020, speed_x: -3, speed_y: -4});
    entries.push(Entry{start_x:  52505, start_y: -52273, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x: -10338, start_y:  21059, speed_x:  1, speed_y: -2});
    entries.push(Entry{start_x: -10341, start_y:  42012, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x:  31566, start_y:  31544, speed_x: -3, speed_y: -3});
    entries.push(Entry{start_x: -52215, start_y: -10360, speed_x:  5, speed_y:  1});
    entries.push(Entry{start_x:  52526, start_y:  21060, speed_x: -5, speed_y: -2});
    entries.push(Entry{start_x:  10638, start_y:  10589, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x:  42034, start_y:  10584, speed_x: -4, speed_y: -1});
    entries.push(Entry{start_x:  31553, start_y: -52264, speed_x: -3, speed_y:  5});
    entries.push(Entry{start_x: -10353, start_y: -10360, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x: -20795, start_y: -31321, speed_x:  2, speed_y:  3});
    entries.push(Entry{start_x: -20830, start_y:  42014, speed_x:  2, speed_y: -4});
    entries.push(Entry{start_x:  10606, start_y: -31319, speed_x: -1, speed_y:  3});
    entries.push(Entry{start_x: -20814, start_y: -41796, speed_x:  2, speed_y:  4});
    entries.push(Entry{start_x: -52239, start_y:  31539, speed_x:  5, speed_y: -3});
    entries.push(Entry{start_x:  31586, start_y:  10586, speed_x: -3, speed_y: -1});
    entries.push(Entry{start_x: -10318, start_y:  31540, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x:  10643, start_y:  10584, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x:  42042, start_y:  10592, speed_x: -4, speed_y: -1});
    entries.push(Entry{start_x: -41749, start_y: -10360, speed_x:  4, speed_y:  1});
    entries.push(Entry{start_x: -41774, start_y:  52490, speed_x:  4, speed_y: -5});
    entries.push(Entry{start_x:  31590, start_y:  31536, speed_x: -3, speed_y: -3});
    entries.push(Entry{start_x: -10350, start_y: -41789, speed_x:  1, speed_y:  4});
    entries.push(Entry{start_x:  42047, start_y: -52264, speed_x: -4, speed_y:  5});
    entries.push(Entry{start_x:  10631, start_y: -20836, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x:  52542, start_y: -52270, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x: -52266, start_y:  21062, speed_x:  5, speed_y: -2});
    entries.push(Entry{start_x: -52258, start_y: -10363, speed_x:  5, speed_y:  1});
    entries.push(Entry{start_x: -41793, start_y:  42016, speed_x:  4, speed_y: -4});
    entries.push(Entry{start_x: -31277, start_y: -10367, speed_x:  3, speed_y:  1});
    entries.push(Entry{start_x:  52510, start_y: -52270, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x: -20842, start_y: -52269, speed_x:  2, speed_y:  5});
    entries.push(Entry{start_x:  10630, start_y: -10362, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x:  21082, start_y:  42011, speed_x: -2, speed_y: -4});
    entries.push(Entry{start_x:  21062, start_y:  52487, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x:  52503, start_y:  31544, speed_x: -5, speed_y: -3});
    entries.push(Entry{start_x:  10587, start_y: -31318, speed_x: -1, speed_y:  3});
    entries.push(Entry{start_x: -41766, start_y:  42015, speed_x:  4, speed_y: -4});
    entries.push(Entry{start_x: -52245, start_y: -52267, speed_x:  5, speed_y:  5});
    entries.push(Entry{start_x: -31277, start_y:  31538, speed_x:  3, speed_y: -3});
    entries.push(Entry{start_x: -10362, start_y:  10583, speed_x:  1, speed_y: -1});
    entries.push(Entry{start_x:  31593, start_y:  52496, speed_x: -3, speed_y: -5});
    entries.push(Entry{start_x:  21108, start_y: -20836, speed_x: -2, speed_y:  2});
    entries.push(Entry{start_x: -52266, start_y:  52490, speed_x:  5, speed_y: -5});
    entries.push(Entry{start_x:  21094, start_y: -10365, speed_x: -2, speed_y:  1});
    entries.push(Entry{start_x:  31575, start_y: -20841, speed_x: -3, speed_y:  2});
    entries.push(Entry{start_x: -31285, start_y:  42013, speed_x:  3, speed_y: -4});
    entries.push(Entry{start_x:  10625, start_y:  10583, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x: -10313, start_y: -52264, speed_x:  1, speed_y:  5});
    entries.push(Entry{start_x:  42036, start_y:  42014, speed_x: -4, speed_y: -4});
    entries.push(Entry{start_x:  31561, start_y:  10589, speed_x: -3, speed_y: -1});
    entries.push(Entry{start_x:  10624, start_y: -41793, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x: -52274, start_y: -31314, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x:  10587, start_y: -10361, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x:  31545, start_y: -41788, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x:  21063, start_y: -20838, speed_x: -2, speed_y:  2});
    entries.push(Entry{start_x: -52234, start_y: -41790, speed_x:  5, speed_y:  4});
    entries.push(Entry{start_x:  52523, start_y:  52490, speed_x: -5, speed_y: -5});
    entries.push(Entry{start_x:  42047, start_y: -10361, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x: -41774, start_y:  10587, speed_x:  4, speed_y: -1});
    entries.push(Entry{start_x: -52274, start_y:  42013, speed_x:  5, speed_y: -4});
    entries.push(Entry{start_x:  21106, start_y:  52494, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x:  52546, start_y: -10360, speed_x: -5, speed_y:  1});
    entries.push(Entry{start_x:  10633, start_y: -20836, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x: -10370, start_y: -20844, speed_x:  1, speed_y:  2});
    entries.push(Entry{start_x:  42030, start_y: -20837, speed_x: -4, speed_y:  2});
    entries.push(Entry{start_x:  21075, start_y:  42020, speed_x: -2, speed_y: -4});
    entries.push(Entry{start_x: -20820, start_y:  21063, speed_x:  2, speed_y: -2});
    entries.push(Entry{start_x:  10622, start_y:  21062, speed_x: -1, speed_y: -2});
    entries.push(Entry{start_x:  42066, start_y:  21065, speed_x: -4, speed_y: -2});
    entries.push(Entry{start_x:  52528, start_y: -52273, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x:  10610, start_y: -31313, speed_x: -1, speed_y:  3});
    entries.push(Entry{start_x: -10370, start_y: -20837, speed_x:  1, speed_y:  2});
    entries.push(Entry{start_x: -20788, start_y:  31535, speed_x:  2, speed_y: -3});
    entries.push(Entry{start_x: -20844, start_y:  52487, speed_x:  2, speed_y: -5});
    entries.push(Entry{start_x:  52510, start_y: -41788, speed_x: -5, speed_y:  4});
    entries.push(Entry{start_x:  31566, start_y: -20844, speed_x: -3, speed_y:  2});
    entries.push(Entry{start_x:  42047, start_y:  42012, speed_x: -4, speed_y: -4});
    entries.push(Entry{start_x: -31282, start_y: -41789, speed_x:  3, speed_y:  4});
    entries.push(Entry{start_x: -41742, start_y:  52493, speed_x:  4, speed_y: -5});
    entries.push(Entry{start_x: -41758, start_y:  21061, speed_x:  4, speed_y: -2});
    entries.push(Entry{start_x:  31579, start_y:  52489, speed_x: -3, speed_y: -5});
    entries.push(Entry{start_x: -31317, start_y:  42013, speed_x:  3, speed_y: -4});
    entries.push(Entry{start_x:  10611, start_y:  21059, speed_x: -1, speed_y: -2});
    entries.push(Entry{start_x:  31535, start_y: -41797, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x: -10338, start_y: -10365, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x: -52261, start_y:  31544, speed_x:  5, speed_y: -3});
    entries.push(Entry{start_x: -10368, start_y: -10369, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x: -41746, start_y:  10587, speed_x:  4, speed_y: -1});
    entries.push(Entry{start_x:  31571, start_y:  31535, speed_x: -3, speed_y: -3});
    entries.push(Entry{start_x: -20786, start_y: -10360, speed_x:  2, speed_y:  1});
    entries.push(Entry{start_x: -52258, start_y:  10584, speed_x:  5, speed_y: -1});
    entries.push(Entry{start_x:  52494, start_y: -31315, speed_x: -5, speed_y:  3});
    entries.push(Entry{start_x: -31317, start_y:  52492, speed_x:  3, speed_y: -5});
    entries.push(Entry{start_x:  31566, start_y: -20839, speed_x: -3, speed_y:  2});
    entries.push(Entry{start_x: -20825, start_y: -52264, speed_x:  2, speed_y:  5});
    entries.push(Entry{start_x:  10614, start_y: -10366, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x: -31277, start_y: -10366, speed_x:  3, speed_y:  1});
    entries.push(Entry{start_x:  52488, start_y:  42020, speed_x: -5, speed_y: -4});
    entries.push(Entry{start_x: -41795, start_y:  31539, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x:  52520, start_y: -52269, speed_x: -5, speed_y:  5});
    entries.push(Entry{start_x:  21070, start_y:  52496, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x: -31293, start_y: -31315, speed_x:  3, speed_y:  3});
    entries.push(Entry{start_x: -10314, start_y:  42016, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x: -20814, start_y: -31319, speed_x:  2, speed_y:  3});
    entries.push(Entry{start_x: -41777, start_y: -52265, speed_x:  4, speed_y:  5});
    entries.push(Entry{start_x:  21079, start_y:  52494, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x:  21101, start_y: -10369, speed_x: -2, speed_y:  1});
    entries.push(Entry{start_x: -20821, start_y:  31537, speed_x:  2, speed_y: -3});
    entries.push(Entry{start_x: -20802, start_y:  21063, speed_x:  2, speed_y: -2});
    entries.push(Entry{start_x:  52531, start_y:  21060, speed_x: -5, speed_y: -2});
    entries.push(Entry{start_x: -20828, start_y:  52496, speed_x:  2, speed_y: -5});
    entries.push(Entry{start_x:  10590, start_y:  52488, speed_x: -1, speed_y: -5});
    entries.push(Entry{start_x:  52511, start_y:  31537, speed_x: -5, speed_y: -3});
    entries.push(Entry{start_x: -20817, start_y: -20839, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x:  21082, start_y:  10587, speed_x: -2, speed_y: -1});
    entries.push(Entry{start_x:  52530, start_y: -31321, speed_x: -5, speed_y:  3});
    entries.push(Entry{start_x: -41782, start_y: -41795, speed_x:  4, speed_y:  4});
    entries.push(Entry{start_x:  42034, start_y: -10360, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x: -41765, start_y: -20841, speed_x:  4, speed_y:  2});
    entries.push(Entry{start_x: -41788, start_y:  42020, speed_x:  4, speed_y: -4});
    entries.push(Entry{start_x:  42047, start_y:  31544, speed_x: -4, speed_y: -3});
    entries.push(Entry{start_x: -31314, start_y: -41793, speed_x:  3, speed_y:  4});
    entries.push(Entry{start_x:  10611, start_y:  31543, speed_x: -1, speed_y: -3});
    entries.push(Entry{start_x:  10611, start_y: -10360, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x:  31542, start_y: -41795, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x:  42050, start_y: -52269, speed_x: -4, speed_y:  5});
    entries.push(Entry{start_x:  31592, start_y:  10592, speed_x: -3, speed_y: -1});
    entries.push(Entry{start_x: -10317, start_y:  21059, speed_x:  1, speed_y: -2});
    entries.push(Entry{start_x:  52544, start_y: -31321, speed_x: -5, speed_y:  3});
    entries.push(Entry{start_x: -31282, start_y:  52488, speed_x:  3, speed_y: -5});
    entries.push(Entry{start_x: -52242, start_y:  31535, speed_x:  5, speed_y: -3});
    entries.push(Entry{start_x: -31290, start_y: -52271, speed_x:  3, speed_y:  5});
    entries.push(Entry{start_x: -52256, start_y: -31312, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x: -31306, start_y: -10364, speed_x:  3, speed_y:  1});
    entries.push(Entry{start_x:  21077, start_y: -20840, speed_x: -2, speed_y:  2});
    entries.push(Entry{start_x:  10598, start_y: -10365, speed_x: -1, speed_y:  1});
    entries.push(Entry{start_x: -41761, start_y: -20837, speed_x:  4, speed_y:  2});
    entries.push(Entry{start_x:  31571, start_y: -31315, speed_x: -3, speed_y:  3});
    entries.push(Entry{start_x: -41772, start_y:  10587, speed_x:  4, speed_y: -1});
    entries.push(Entry{start_x: -41750, start_y:  21067, speed_x:  4, speed_y: -2});
    entries.push(Entry{start_x:  31539, start_y: -31314, speed_x: -3, speed_y:  3});
    entries.push(Entry{start_x:  10619, start_y:  10590, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x: -10341, start_y:  31539, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x: -20814, start_y: -52268, speed_x:  2, speed_y:  5});
    entries.push(Entry{start_x: -20814, start_y:  21066, speed_x:  2, speed_y: -2});
    entries.push(Entry{start_x:  10614, start_y:  10585, speed_x: -1, speed_y: -1});
    entries.push(Entry{start_x: -41774, start_y:  21061, speed_x:  4, speed_y: -2});
    entries.push(Entry{start_x:  10622, start_y: -20840, speed_x: -1, speed_y:  2});
    entries.push(Entry{start_x: -41793, start_y:  31541, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x: -20841, start_y:  21061, speed_x:  2, speed_y: -2});
    entries.push(Entry{start_x:  10622, start_y: -41792, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x: -31317, start_y:  10590, speed_x:  3, speed_y: -1});
    entries.push(Entry{start_x: -10341, start_y: -10369, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x: -31322, start_y:  42018, speed_x:  3, speed_y: -4});
    entries.push(Entry{start_x: -20838, start_y: -20840, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x: -20844, start_y: -10360, speed_x:  2, speed_y:  1});
    entries.push(Entry{start_x:  10634, start_y: -41789, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x:  42010, start_y:  52496, speed_x: -4, speed_y: -5});
    entries.push(Entry{start_x: -41777, start_y:  31542, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x:  10602, start_y: -31316, speed_x: -1, speed_y:  3});
    entries.push(Entry{start_x:  52538, start_y:  42015, speed_x: -5, speed_y: -4});
    entries.push(Entry{start_x:  21083, start_y:  52489, speed_x: -2, speed_y: -5});
    entries.push(Entry{start_x:  21066, start_y:  21060, speed_x: -2, speed_y: -2});
    entries.push(Entry{start_x: -20805, start_y: -41793, speed_x:  2, speed_y:  4});
    entries.push(Entry{start_x:  21087, start_y: -41788, speed_x: -2, speed_y:  4});
    entries.push(Entry{start_x:  52514, start_y:  21066, speed_x: -5, speed_y: -2});
    entries.push(Entry{start_x:  52515, start_y: -41790, speed_x: -5, speed_y:  4});
    entries.push(Entry{start_x:  21066, start_y: -31313, speed_x: -2, speed_y:  3});
    entries.push(Entry{start_x: -41753, start_y: -52272, speed_x:  4, speed_y:  5});
    entries.push(Entry{start_x:  10587, start_y:  31537, speed_x: -1, speed_y: -3});
    entries.push(Entry{start_x: -20814, start_y: -31312, speed_x:  2, speed_y:  3});
    entries.push(Entry{start_x:  10627, start_y:  52488, speed_x: -1, speed_y: -5});
    entries.push(Entry{start_x:  52523, start_y: -20837, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x: -41774, start_y:  52492, speed_x:  4, speed_y: -5});
    entries.push(Entry{start_x: -52269, start_y:  21062, speed_x:  5, speed_y: -2});
    entries.push(Entry{start_x: -31282, start_y:  10583, speed_x:  3, speed_y: -1});
    entries.push(Entry{start_x: -31322, start_y:  21059, speed_x:  3, speed_y: -2});
    entries.push(Entry{start_x: -31302, start_y: -20845, speed_x:  3, speed_y:  2});
    entries.push(Entry{start_x:  52526, start_y: -10360, speed_x: -5, speed_y:  1});
    entries.push(Entry{start_x:  31536, start_y: -41793, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x: -20809, start_y:  42015, speed_x:  2, speed_y: -4});
    entries.push(Entry{start_x:  31542, start_y: -52271, speed_x: -3, speed_y:  5});
    entries.push(Entry{start_x:  52486, start_y: -10363, speed_x: -5, speed_y:  1});
    entries.push(Entry{start_x: -10311, start_y:  42011, speed_x:  1, speed_y: -4});
    entries.push(Entry{start_x: -41761, start_y:  10584, speed_x:  4, speed_y: -1});
    entries.push(Entry{start_x:  42050, start_y: -41789, speed_x: -4, speed_y:  4});
    entries.push(Entry{start_x:  52515, start_y: -20838, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x:  21058, start_y: -20841, speed_x: -2, speed_y:  2});
    entries.push(Entry{start_x:  31586, start_y: -31320, speed_x: -3, speed_y:  3});
    entries.push(Entry{start_x: -41766, start_y:  31541, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x: -41769, start_y:  31540, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x: -52250, start_y: -31320, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x:  52543, start_y:  42020, speed_x: -5, speed_y: -4});
    entries.push(Entry{start_x:  42052, start_y: -20841, speed_x: -4, speed_y:  2});
    entries.push(Entry{start_x:  52499, start_y:  31544, speed_x: -5, speed_y: -3});
    entries.push(Entry{start_x:  52515, start_y: -20842, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x:  31537, start_y:  31535, speed_x: -3, speed_y: -3});
    entries.push(Entry{start_x:  52490, start_y: -20836, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x:  52518, start_y:  21066, speed_x: -5, speed_y: -2});
    entries.push(Entry{start_x:  31590, start_y:  52492, speed_x: -3, speed_y: -5});
    entries.push(Entry{start_x: -10310, start_y: -10369, speed_x:  1, speed_y:  1});
    entries.push(Entry{start_x:  31582, start_y:  42019, speed_x: -3, speed_y: -4});
    entries.push(Entry{start_x: -10368, start_y: -52269, speed_x:  1, speed_y:  5});
    entries.push(Entry{start_x:  31539, start_y: -20844, speed_x: -3, speed_y:  2});
    entries.push(Entry{start_x:  10590, start_y: -41796, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x:  52538, start_y: -20837, speed_x: -5, speed_y:  2});
    entries.push(Entry{start_x: -41737, start_y:  31543, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x: -52271, start_y: -31312, speed_x:  5, speed_y:  3});
    entries.push(Entry{start_x:  31559, start_y:  42012, speed_x: -3, speed_y: -4});
    entries.push(Entry{start_x: -10330, start_y:  31542, speed_x:  1, speed_y: -3});
    entries.push(Entry{start_x: -41797, start_y:  31539, speed_x:  4, speed_y: -3});
    entries.push(Entry{start_x:  10639, start_y:  52487, speed_x: -1, speed_y: -5});
    entries.push(Entry{start_x:  31566, start_y: -41792, speed_x: -3, speed_y:  4});
    entries.push(Entry{start_x:  42068, start_y:  42020, speed_x: -4, speed_y: -4});
    entries.push(Entry{start_x:  42066, start_y: -20840, speed_x: -4, speed_y:  2});
    entries.push(Entry{start_x:  10583, start_y: -52264, speed_x: -1, speed_y:  5});
    entries.push(Entry{start_x:  21066, start_y:  31543, speed_x: -2, speed_y: -3});
    entries.push(Entry{start_x:  10606, start_y: -41790, speed_x: -1, speed_y:  4});
    entries.push(Entry{start_x:  42042, start_y: -41793, speed_x: -4, speed_y:  4});
    entries.push(Entry{start_x:  42038, start_y: -31314, speed_x: -4, speed_y:  3});
    entries.push(Entry{start_x: -20806, start_y: -20842, speed_x:  2, speed_y:  2});
    entries.push(Entry{start_x:  42010, start_y: -10366, speed_x: -4, speed_y:  1});
    entries.push(Entry{start_x: -41795, start_y: -20841, speed_x:  4, speed_y:  2});
    entries.push(Entry{start_x:  10633, start_y:  21059, speed_x: -1, speed_y: -2});
    entries.push(Entry{start_x:  52527, start_y: -10369, speed_x: -5, speed_y:  1});
    entries.push(Entry{start_x:  21109, start_y: -31312, speed_x: -2, speed_y:  3});
    entries.push(Entry{start_x: -52224, start_y:  52496, speed_x:  5, speed_y: -5});
    entries.push(Entry{start_x:  10583, start_y:  10592, speed_x: -1, speed_y: -1});

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

    let vertex1 = Vertex { position: [-1.0, -1.0], tex_coords: [0.0, 1.0] };
    let vertex2 = Vertex { position: [-1.0,  1.0], tex_coords: [0.0, 0.0] };
    let vertex3 = Vertex { position: [ 1.0, -1.0], tex_coords: [1.0, 1.0] };

    let vertex4 = Vertex { position: [ 1.0,  1.0], tex_coords: [1.0, 0.0] };
    let vertex5 = Vertex { position: [-1.0,  1.0], tex_coords: [0.0, 0.0] };
    let vertex6 = Vertex { position: [ 1.0, -1.0], tex_coords: [1.0, 1.0] };

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

    let t : i64 = 10450;
    let mut mx = 0;
            
    let w: i64 = 640;
    let h: i64 = 480;

    let mut data = vec![0 as u8; (3*w*h) as usize];

    let mut closed = false;
    while !closed {

        //t += 1;

        for d in &mut data {
            *d = 0;
        }

        for e in &entries {
            let x = e.start_x + ((t + mx) * e.speed_x);
            let y = e.start_y + ((t + mx) * e.speed_y);

            if x >= 0 && x < w && y >= 0 && y < h {
                let coord = (3*x + 3*y*w) as usize;
                data[coord + 0] = 255;
                data[coord + 1] = 255;
                data[coord + 2] = 255;
            }
        }

        println!("t: {} s", t+mx);

        let raw = RawImage2d {
            data: Cow::Borrowed(&data),
            width: w as u32,
            height: h as u32,
            format: ClientFormat::U8U8U8,
        };

        let texture = glium::texture::Texture2d::new(&display, raw).unwrap();

        let mut target = display.draw();

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
                    glutin::WindowEvent::CursorMoved {
                        device_id: _,
                        position,
                        modifiers: _,
                    } => {
                        mx = position.x as i64;
                    }
                    _ => (),
                },
                _ => (),
            }
        });
    }
}
