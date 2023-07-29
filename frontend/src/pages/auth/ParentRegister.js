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
} from "@mantine/core";
import { IconAt } from "@tabler/icons-react";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";
import axios from "axios";
import {useAuth} from '../../context/auth-context'

export default function ParentRegister() {
  const {register} = useAuth()
  const [searchValue, onSearchChange] = useState("");
  const [loading, setLoading] = useState(false);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassowrd] = useState("");

  const passwordMatch = password === confirmPassword;


  const handleRegister = async () => {
    const data = {
      phone_number: phoneNumber,
      email: email,
      account_type: "parent",
      password: password,
      role : "parent",
      active: true,
      verified: false,
      suspended: false,
    };
    await register(data);
  };


  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <SignupHead title="Parent" />
        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="First Name"
            my="md"
            value={firstName}
            onChange={(event) => setFirstName(event.currentTarget.value)}
            required />
          <TextInput label="Last Name"
            my="md"
            value={lastName}
            onChange={(event) => setLastName(event.currentTarget.value)}
            required />
          <TextInput
            type="number"
            label="Phone Number"
            my="md"
            value={phoneNumber}
            onChange={(event) => setPhoneNumber(event.currentTarget.value)}
            icon={<Text color="gray" ml="xr"> +237</Text>}
            required
          />
          <TextInput
            label="Email"
            placeholder="you@mantine.dev"
            my="md"
            value={email}
            onChange={(event) => setEmail(event.currentTarget.value)}
            icon={<IconAt size="0.8rem" />}
            required />
          <PasswordInput
            label="Password"
            my="md"
            required
            value={password}
            onChange={(event) => setPassword(event.currentTarget.value)}

          />
          <PasswordInput
            label="Confirm Password"
            my="md"
            required
            mt="md"
            value={confirmPassword}
            onChange={(event) => setConfirmPassowrd(event.currentTarget.value)}
          />
          {
            (!passwordMatch && confirmPassword )&& (
              <Text color="red" mt="md">Passwords do not match</Text>
            )
          }
          <Button
            fullWidth
            mt="xl"
            style={{
              backgroundColor: "#FFC107",
            }}
          >
            Sign in
          </Button>
        </Paper>
      </Container>
    </div>
  );
}
