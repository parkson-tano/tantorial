import React, { useState, useEffect } from "react";
import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
  Select,
  Box
} from "@mantine/core";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";
import { useForm, isNotEmpty, isEmail, isInRange, hasLength, matchesField } from '@mantine/form';
import { API_URL, fetchClasses, fetchSchools, fetchSubsystems } from "../../constant";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { registerUser, updateUserProfile } from "../../actions/auth";

export default function StudentRegister() {
  const navigate = useNavigate();
  const [subsystems, setSubsystems] = useState([]);
  const [schools, setSchools] = useState([]);
  const [classes, setClasses] = useState([]);
  const form = useForm({
    initialValues: {
      firstName: '',
      lastName: '',
      subsystem: '',
      school: '',
      class: '',
      password: '',
      confirmPassword: '',

    },
    validate: {
      firstName: hasLength({ min: 3 }, 'First name must be at least 3 characters long'),
      lastName: hasLength({ min: 3 }, 'Last name must be at least 3 characters long'),
      subsystem: isNotEmpty('Please select a subsystem'),
      school: isNotEmpty('Please select a school'),
      class: isNotEmpty('Please select a class'),
      password: hasLength({ min: 6 }, 'Password must be at least 6 characters long'),
      confirmPassword: matchesField('password', 'Passwords are not the same'),
    }
  });

  const handleRegister = async () => {
    const data = {
      first_name: form.values.firstName,
      last_name: form.values.lastName,
      password: form.values.password,
      email: `${form.values.firstName.toLowerCase()}.${form.values.lastName.toLowerCase()}@tantorial.ng`,
      phone_number: "00000000000",
      verified: false,
      account_type: "student",
      suspended: false,
      active: true,
      admin: false,
      role: "student",
    };

    try {
      registerUser(data)
        .then(user => {
          const profileData = {
            first_name: form.values.firstName,
            last_name: form.values.lastName,
            // language: form.values.subsystem,
            school: form.values.school,
            subsystem: form.values.subsystem,
            student_class: form.values.class,
          };
          const profile = updateUserProfile(user, profileData);
          navigate('/login');

        })
    } catch (error) {
      console.error('Registration error:', error.message);
    }
  };

  useEffect(() => {
    const fetchSubsystemsAndSchools = async () => {
      try {
        const [subsystemsData, schoolsData, classesData] = await Promise.all([
          fetchSubsystems(),
          fetchSchools(),
          fetchClasses()
        ]);

        setSubsystems(subsystemsData);
        // const filter_school = schoolsData.filter(item => item.subsystem === form.values.subsystem);
        setSchools(schoolsData);
        // Filter classes based on the selected school
        const filter_class = classesData.filter(item => item.school === form.values.school);
        setClasses(filter_class);
      } catch (error) {
        console.error('Error fetching data:', error.message);
      }
    };
    fetchSubsystemsAndSchools();
  }, [form.values.school]); // Dependency on form.values.school



  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <Box component="form" maw={400} mx="auto" onSubmit={form.onSubmit(handleRegister)}>
          <SignupHead title="Student" />

          <Paper withBorder shadow="md" p={30} mt={30} radius="md">
            <TextInput label="First Name"
              {...form.getInputProps('firstName')}
            />
            <TextInput label="Last Name"
              {...form.getInputProps('lastName')}
            />
            <Select
              mt="md"
              label="Subsystem"
              data={subsystems}
              rightSection={<IconChevronDown size="1rem" />}
              {...form.getInputProps('subsystem')}
              placeholder="Select Subsystem"
            />
            <Select
              mt="md"
              label="Your School"
              searchable
              rightSection={<IconChevronDown size="1rem" />}
              nothingFound="Your School is not listed"
              data={schools}
              {...form.getInputProps('school')}
            />
            <Select
              mt="md"
              label="Your Class"
              rightSection={<IconChevronDown size="1rem" />}
              data={classes}
              {...form.getInputProps('class')}
            />
            <PasswordInput
              label="Password"
              {...form.getInputProps('password')}
              mt="md"
            />
            <PasswordInput
              label="Confirm Password"
              {...form.getInputProps('confirmPassword')}
              mt="md"
            />
            <Button
              type="submit"
              fullWidth
              mt="xl"
              style={{
                backgroundColor: "#FFC107",
              }}
            >
              Sign in
            </Button>
          </Paper>
        </Box>
      </Container>
    </div>
  );
}
