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
import { registerUser } from "../../actions/auth";
import { useForm, isNotEmpty, isEmail, isInRange, hasLength, matchesField } from '@mantine/form';

export default function ParentRegister() {
  const navigate = useNavigate();
  const [searchValue, onSearchChange] = useState("");
  const [loading, setLoading] = useState(false);

  const form = useForm({
    initialValues: {
      firstName: '',
      lastName: '',
      phoneNumber: '',
      email: '',
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
      account_type: "parent",
      suspended: false,
      active: true,
      admin: false,
      role: "parent"
    };

    try {
      const userId = await registerUser(data); // Assuming registerUser returns the user ID
      console.log('User ID:', userId); // Log the user ID
      navigate('/login');
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
          <SignupHead title="Parent" />
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
              {...form.getInputProps('phoneNumber')}
              icon={<Text color="gray" ml="xr"> +237</Text>}

            />

            <TextInput
              label="Email"
              placeholder="you@mantine.dev"
              my="md"
              icon={<IconAt size="0.8rem" />}
              {...form.getInputProps('email')}
            />

            <PasswordInput
              label="Password"
              my="md"
              {...form.getInputProps('password')}

            />

            <PasswordInput
              label="Confirm Password"
              my="md"

              mt="md"
              {...form.getInputProps('confirmPassword')}
            />

            <Button
              fullWidth
              mt="xl"
              style={{
                backgroundColor: "#FFC107",
              }}
              type="submit"
            >
              Sign in
            </Button>
          </Paper>
        </Box>
      </Container>
    </div>
  );
}
