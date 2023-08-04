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
  Box,
  Select,
} from "@mantine/core";
import { IconAt } from "@tabler/icons-react";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useAuth } from '../../context/auth-context'
import { registerUser, updateUserProfile } from "../../actions/auth";
import { useForm, isNotEmpty, isEmail, isInRange, hasLength, matchesField } from '@mantine/form';

export default function TeacherRegister() {
  const navigate = useNavigate();
  const [schoolTeacher, setSchoolTeacher] = useState(false);

  const form = useForm({
    initialValues: {
      firstName: '',
      lastName: '',
      phoneNumber: '',
      email: '',
      school_teacher: false,
      subsystem: '',
      school: '',
      password: '',
      confirmPassword: '',

    },
    validate: {
      firstName: hasLength({ min: 3 }, 'First name must be at least 3 characters long'),
      lastName: hasLength({ min: 3 }, 'Last name must be at least 3 characters long'),
      phoneNumber: hasLength({ min: 9, max: 9 }, 'Phone number must be 9 Digits long'),
      email: isEmail('Please enter a valid email'),
      password: hasLength({ min: 6 }, 'Password must be at least 6 characters long'),
      confirmPassword: matchesField('password', 'Passwords are not the same'),
    }
  });

  const handleRegister = async () => {
    const data = {
      first_name: form.values.firstName,
      last_name: form.values.lastName,
      phone_number: form.values.phoneNumber,
      email: form.values.email,
      password: form.values.password,
      verified: false,
      account_type: "teacher",
      suspended: false,
      active: true,
      admin: false,
      role: "teacher"
    };
    try {
      registerUser(data)
        .then(user => {
          const profileData = {
            first_name: form.values.firstName,
            last_name: form.values.lastName,
            phone_number: form.values.phoneNumber,
            // school  : form.values.school,
            // subsystem: form.values.subsystem,
          };
          const profile = updateUserProfile(user, profileData);
          navigate('/login');

        })
    } catch (error) {
      console.error('Registration error:', error.message);
    }
  };




  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <Box component="form" maw={400} mx="auto" onSubmit={form.onSubmit(handleRegister)}>
          <SignupHead title="Teacher" />
          <Paper withBorder shadow="md" p={30} mt={30} radius="md">
            <TextInput label="First Name"
              my="md"
              {...form.getInputProps('firstName')}
            />
            <TextInput label="Last Name"
              my="md"
              {...form.getInputProps('lastName')}
            />
            <TextInput
              type="number"
              label="Phone Number"
              my="md"
              icon={<Text color="gray" ml="xr"> +237</Text>}
              {...form.getInputProps('phoneNumber')}
            />
            <TextInput
              label="Email"
              placeholder="you@mantine.dev"
              icon={<IconAt size="0.8rem" />}
              {...form.getInputProps('email')}
            />
            <Checkbox label="I am a school teacher"
              my="md"
              {...form.getInputProps('school_teacher')}
            />
            {
              form.values.school_teacher && (
                <>
                  <Select
                    mt="md"
                    label="Subsystem"
                    data={['English', 'French', 'Both']}
                    placeholder="Select Subsystem"
                    rightSection={<IconChevronDown size="1rem" />}
                    {...form.getInputProps('subsystem')}
                    my="md"
                  />
                  <Select
                    mt="md"
                    label="Your School"
                    searchable
                    nothingFound="Your School is not listed"
                    my="md"
                    rightSection={<IconChevronDown size="1rem" />}
                    data={["React", "Angular", "Svelte", "Vue"]}
                    {...form.getInputProps('school')}
                  />
                </>
              )
            }
            <PasswordInput
              label="Password"
              my="md"
              {...form.getInputProps('password')}
              mt="md"
            />
            <PasswordInput
              label="Confirm Password"
              my="md"
              {...form.getInputProps('confirmPassword')}
              mt="md"
            />
            <Button
              fullWidth
              mt="xl"
              type="submit"
              style={{
                backgroundColor: "#FFC107",
              }}
            >
              Register
            </Button>
          </Paper>
        </Box>
      </Container>
    </div>
  );
}
