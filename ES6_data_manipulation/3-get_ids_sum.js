export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const initialValue = 0;
  return students.reduce((accumulator, student) => accumulator + student.id, initialValue);
}
